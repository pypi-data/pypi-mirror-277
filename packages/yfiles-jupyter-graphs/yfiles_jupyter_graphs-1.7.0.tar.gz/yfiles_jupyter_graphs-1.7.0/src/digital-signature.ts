import { LicenseJson } from './typings'

// ask Jupyter Widget admins for the corresponding private key
const PUBLIC_KEY = `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5uUZk31RXPPFlM3/BdJs
2+Coi7sx969FlaZCFJFnGYtQ497xZc+uWvPJEDwDbY9/S6a60ex3STRGJMveMS/K
X8gxLecFo8iJYq45ahF7LP3qc+kCK7jGkjQwfrhYTLcW4Fe4tqgKjxAcvkCy40UF
2Pvkg7Ash7ZUKMprkrKBOrk5C6y95zSnypvKIJNt2M76Ec6SZkGNVVKqV264LFTC
uSFrwH7U90UJWjWFe2rpySWvDGdTCrBTgbW4M9tldd7qlPfIpzh4s0d3fdCcwuMT
Rdsp5DoX1SPKflmaQSTV3q6lavJ9HRRU/dl5pOIW7+LK4cuubYaivuAT2IDl7LXL
XQIDAQAB
-----END PUBLIC KEY-----`

const algoName = 'RSASSA-PKCS1-v1_5'
const algoHash = 'SHA-256'
const publicKeyFormat = 'spki'

/**
 * Verifies a given message with the signature.
 */
export async function verifyMessage(
  licenseJson: LicenseJson,
  signature: Uint8Array
): Promise<boolean> {
  const importedPublicKey = await importPublicKey()
  const data = new TextEncoder().encode(JSON.stringify(licenseJson))

  return await crypto.subtle.verify(
    {
      name: algoName,
      hash: { name: algoHash },
    },
    importedPublicKey,
    signature,
    data
  )
}

/**
 * Converts the public key to the correct format and returns a cryptoKey promise
 */
function importPublicKey(): Promise<CryptoKey> {
  const binaryDerString = atob(extractKeyContent(PUBLIC_KEY))
  const binaryDer = Uint8Array.from(binaryDerString, (char) =>
    char.charCodeAt(0)
  )

  return crypto.subtle.importKey(
    publicKeyFormat,
    binaryDer,
    { name: algoName, hash: { name: algoHash } },
    false,
    ['verify']
  )
}

function extractKeyContent(key: string): string {
  const header = '-----BEGIN PUBLIC KEY-----'
  const footer = '-----END PUBLIC KEY-----'
  return key.replace(header, '').replace(footer, '').replace(/\n/g, '').trim()
}
