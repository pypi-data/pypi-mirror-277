import './style.css'
import { v4 as uuid } from 'uuid'

const LICENSE_SERVER_ENDPOINT = 'http://localhost:8080/generate-digest'

const mainContainer = document.getElementById('app') as HTMLDivElement
mainContainer.id = 'app'

const licenseBoxHtml = `
    <div class="license-box">
        <div class="input-container">
            <label for="version">Select a version:</label>
   
            <select name="version" id="version" required>
                <option value="1.0"> version 1.0</option>
            </select>
        </div>

        <div class="input-container">
            <label for="domains">domains:</label>

            <input type="text" id="domain-list" name="domain-list" size="30"  placeholder="yworks.com" required />
        </div>

        <div class="input-container">
            <label for="expiry"> expiry date:</label>
    
            <input type="date" id="expiry-date" required>
        </div>
        
    </div>
`
const licenseBox = document.createElement('div')
licenseBox.innerHTML = licenseBoxHtml
mainContainer.appendChild(licenseBox)

const buttonContainer = document.createElement('div')
buttonContainer.classList.add('button')

const warningMessage = document.createElement('div')
warningMessage.textContent = 'Please correctly fill in all required fields.'
warningMessage.classList.add('warning-message')
licenseBox.appendChild(warningMessage)

// Create button element
const submitBtn = document.createElement('button')
submitBtn.type = 'button'
submitBtn.id = 'submitBtn'
submitBtn.textContent = 'generate license'

const versionSelectionElement = document.getElementById(
  'version'
) as HTMLSelectElement
const domainInputElement = document.getElementById(
  'domain-list'
) as HTMLInputElement
const expiryInputElement = document.getElementById(
  'expiry-date'
) as HTMLInputElement

submitBtn.addEventListener('click', async () => {
  const versionSelect = versionSelectionElement.value
  const domainInput = domainInputElement.value
  const expiryInput = expiryInputElement.value
  if (
    versionSelect.trim() !== '' &&
    domainInput.trim() !== '' &&
    expiryInput.trim() !== ''
  ) {
    warningMessage.style.display = 'None'
    //license values
    const value = getJsonValues()
    //add signature to the license data
    value[0].signature = await sendPostRequest(value[0])
    download(JSON.stringify(value[0], null, 2), 'license.json')
  } else {
    warningMessage.style.display = 'block'
  }
})

buttonContainer.appendChild(submitBtn)

mainContainer.appendChild(buttonContainer)
document.body.appendChild(mainContainer)

//generates a JSON with the given data and private Key
function getJsonValues(): Record<string, any> {
  const id = uuid()
  const versionSelect = versionSelectionElement.value
  const domainInput = domainInputElement.value
  const expiryInput = expiryInputElement.value
  const domainsArray = domainInput
    .split(',')
    .map((domain: string) => domain.trim())
  const filteredArray = domainsArray.filter((domain: string) => domain !== '')

  return [
    {
      id: id,
      domains: filteredArray,
      expiry: expiryInput,
      version: versionSelect,
    },
  ]
}

//creates a downloaded json file of the signed license, usable in the jupyter notebook cells
function download(content: any, fileName: string) {
  const a = document.createElement('a')
  const file = new Blob([content], { type: 'application/json' })
  a.href = URL.createObjectURL(file)
  a.download = fileName
  a.click()
}

function sendPostRequest(data: Record<string, any>) {
  return fetch(LICENSE_SERVER_ENDPOINT, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    mode: 'cors',
  })
    .then((response) => response.json())
    .then((result) => {
      //nodejs result
      return result
    })
    .catch((error) => {
      console.error('Error:', error)
    })
}
