const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const path = require('path')
const crypto = require('crypto')

require('dotenv').config()

const privateKey = process.env.PKCS8_PRIVATE_KEY

if (!privateKey) {
  throw new Error(
    'PKCS8_PRIVATE_KEY not found. Make sure to set the PKCS8_PRIVATE_KEY env variable.'
  )
}

function extractKeyContent(key) {
  const header = '-----BEGIN PRIVATE KEY-----'
  const footer = '-----END PRIVATE KEY-----'
  return key
    .replace(header, '')
    .replace(footer, '')
    .replace(/[\n|\s]/g, '')
    .trim()
}

function signJSONWithPrivateKey(jsonInput) {
  // Get the private key from an environment variable
  const privateKeyBytes = atob(extractKeyContent(privateKey))
  const key = Uint8Array.from(
    Array.from(privateKeyBytes).map((char) => char.charCodeAt(0))
  )
  let privateKeyPem = crypto.createPrivateKey({
    key,
    format: 'der',
    type: 'pkcs8',
  })

  // Convert JSON input to a string
  let jsonStr = JSON.stringify(jsonInput)

  // Create a sign object
  let sign = crypto.createSign('SHA256')
  sign.update(jsonStr)

  // Sign the data and return as hex format
  return sign.sign(privateKeyPem, 'hex')
}

function addSignatureToJson(json) {
  json.signature = signJSONWithPrivateKey(json)
}

const app = express()
app.use(cors())

app.use(bodyParser.json())

const swaggerExpress = require('swagger-express-mw')

swaggerExpress.create({ appRoot: __dirname }, (err, swaggerExpress) => {
  if (err) {
    throw err
  }

  swaggerExpress.register(app)
})

app.post('/generate-digest', (req, res) => {
  const jsonInput = req.body
  if (!jsonInput) {
    return res.status(400).send('Invalid Input')
  }

  // Your logic for generating message digest
  const messageDigest = signJSONWithPrivateKey(jsonInput)

  res.status(200).json(messageDigest)
})

const swaggerUi = require('swagger-ui-express')
const YAML = require('yamljs')

const swaggerDocument = YAML.load(
  path.resolve(__dirname, './api/swagger/swagger.yaml')
)

app.use('/docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument))

const PORT = process.env.PORT || 8080
app.listen(PORT, () => console.log(`Server running on port ${PORT}`))
