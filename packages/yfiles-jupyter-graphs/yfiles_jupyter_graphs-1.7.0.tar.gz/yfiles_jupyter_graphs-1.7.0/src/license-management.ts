import license from './yfiles-license.json'
import { showToast } from './utils'
import { LicenseJson, SignedLicenseJson } from './typings'
import { verifyMessage } from './digital-signature'
/**
 * License reminder is shown if the license expires in <= this number of days.
 */
const LICENSE_REMINDER_THRESHOLD = 150
const CONTINUE_EXPIRATION_DAYS = 7
/**
 * License consent is stored in local storage
 */
const LICENSE_CONSENT_KEY = 'yjg.license-accepted'

const CONTINUE_CONSENT_KEY = 'yjg.continue-accepted'

// https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28
const allowedHostnameRegexps: RegExp[] = [
  /^192\./,
  /^127\.0\.0\.1$/,
  /^localhost$/,
  /vscode.dev$/,
  /mybinder\.ovh$/, // support for binder repositories https://binder.mybinder.ovh/, typical hostname: hub-binder.mybinder.ovh
  /colab\.googleusercontent\.com$/, // google colaboratory, typical hostname: 'w8sx1kylgm-496ff2e9c6d22116-0-colab.googleusercontent.com'
  /notebooks\.googleusercontent\.com/, // Google Vertex AI Workbench Notebooks https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28#discussioncomment-6189301
  /dataproc\.googleusercontent\.com/, // Google's DataProc Jupyter notebooks https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28#discussioncomment-6306412
  /kaggle/, // kaggle.com, typical hostname: kkb-production.jupyter-proxy.kaggle.net
  /domino/, // Domino Data Lab, https://github.com/yWorks/yfiles-jupyter-graphs/issues/29
  /kubeflow/, // Kubernetes Cluster with Kubeflow on AWS
  /ml\.azure\.com/, // azure, https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28#discussioncomment-5759349
  /notebooks\.azuresandbox\.ms/, //azure, https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28#discussioncomment-5759349
  /sagemaker\.aws/, // AWS SageMaker https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28#discussioncomment-5884220
  /apps\.sciserver\.org/, // Johns Hopkins University https://github.com/yWorks/yfiles-jupyter-graphs/discussions/28#discussioncomment-6173853
]

export const isAllowedHostname = allowedHostnameRegexps.some((regexp) =>
  regexp.test(location.hostname)
)

// @yjs:keep=origin
export const isVsCodeEnv = location.origin.startsWith('vscode-webview')

// @yjs:keep=origin
export const isGoogleColabEnv = location.origin.includes(
  'colab.research.google.com'
)

export function getRemainingLicenseDays(): number {
  const expires = (license as any).expires
  if (!expires) {
    return LICENSE_REMINDER_THRESHOLD + 1
  }
  const expirationDate = new Date(expires).getTime()
  const diff = expirationDate - Date.now()
  return (diff / (60 * 60 * 24 * 1000)) | 0
}

export function initializeUpdateReminder(parent: HTMLDivElement): void {
  const remainingLicenseDays = getRemainingLicenseDays()

  if (remainingLicenseDays <= LICENSE_REMINDER_THRESHOLD) {
    // if the license is entirely expired, there'll be another screen on the start
    const text = 'Free license expiring soon. Please update this widget.'
    showToast(parent, text)
  }
}

export function checkLicenseConsent(parent: HTMLDivElement): void {
  // check local storage
  try {
    const item = localStorage.getItem(LICENSE_CONSENT_KEY)
    if (item) {
      // license was accepted earlier
      return
    }
  } catch (e) {
    /* do nothing */
  }

  const text =
    "By using this extension, you are accepting the <a href='https://github.com/yWorks/yfiles-jupyter-graphs/blob/master/LICENSE.md' target='_blank'>license terms</a>."
  const licenseTermsToast = showToast(
    parent,
    text,
    () => {
      try {
        localStorage.setItem(LICENSE_CONSENT_KEY, String(new Date().getTime()))
        window.dispatchEvent(new Event(LICENSE_CONSENT_KEY))
      } catch (e) {
        /* do nothing */
      }
    },
    true
  )

  // listen for the consent event to close the activation in each loaded widget (e.g. multiple widget in same notebook)
  window.addEventListener(LICENSE_CONSENT_KEY, () => {
    licenseTermsToast.classList.remove('show-toast')
  })
}

export function isValidHostname(): boolean {
  return isAllowedHostname || isVsCodeEnv
}

/**
 * @yjs:keep=origin,data
 */
export function showInvalidHostMessage(
  widgetRootElement: HTMLDivElement
): HTMLDivElement {
  const hostnameInfo = document.createElement('div') as HTMLDivElement
  hostnameInfo.className = 'fullscreen-warning'

  const message = document.createElement('div')
  message.className = 'warning-message'
  message.innerHTML =
    '<p>You are running yFiles Graphs for Jupyter on <code>' +
    location.origin +
    '</code>.</p>' +
    '<p>The widget only permits use on <code>127.0.0.1</code> and <code>localhost</code>.</p>' +
    "<p>In case this doesn't work for you, let us know the above-mentioned location on " +
    '<a href="https://github.com/yWorks/yfiles-jupyter-graphs/discussions/" target="_blank">GitHub</a>.</p>'

  const ywSide = document.createElement('iframe')
  ywSide.className = 'yw-frame'
  window.addEventListener('message', (evt: any) => {
    if (evt?.origin.indexOf('yworks.com') !== -1 && evt?.data === 'continue') {
      try {
        localStorage.setItem(CONTINUE_CONSENT_KEY, String(Date.now()))
      } catch (e) {
        // do nothing
      }
      hostnameInfo.classList.remove('show')
      widgetRootElement.classList.remove('show-iframe-backdrop')
      ywSide.parentElement?.removeChild(ywSide)
    }
  })
  ywSide.src = 'https://www.yworks.com/products/yfiles-graphs-for-jupyter/trial'

  const continueButton = document.createElement('button')
  continueButton.className = 'continue-button'
  continueButton.innerHTML =
    '<span style="display: block;">Click for free license</span>' +
    '<span style="font-size: 12px; margin-top: 4px;">obtains a free temporary license from yworks.com</span>'
  continueButton.addEventListener('click', () => {
    hostnameInfo.classList.remove('show')
    widgetRootElement.classList.add('show-iframe-backdrop')
  })

  message.appendChild(continueButton)

  const note = document.createElement('p')
  note.innerHTML =
    'In case you need a specific license for your domain, <a href="mailto:contact@yworks.com?subject=yFiles Graphs For Jupyter - Domain license request">email</a> us.'
  message.appendChild(note)

  hostnameInfo.appendChild(message)
  widgetRootElement.appendChild(ywSide)
  widgetRootElement.appendChild(hostnameInfo)

  hostnameInfo.classList.add('show')

  return hostnameInfo
}

export function showExpiredYfilesLicenseMessage(
  widgetRootElement: HTMLDivElement
): void {
  const expiredLicense = document.createElement('div') as HTMLDivElement
  expiredLicense.className = 'fullscreen-warning'
  const message = document.createElement('div')
  message.className = 'warning-message'
  message.innerHTML =
    '<p>The license of this widget has expired.</p>' +
    '<p>To update the license, please install the new free version of the widget from the ' +
    '<a href="https://pypi.org/" target="_blank">Python Package Index</a>.</p>' +
    "<p>In case this doesn't work for you, let us know on " +
    '<a href="https://github.com/yWorks/yfiles-jupyter-graphs/issues" target="_blank">GitHub</a>.</p>'
  expiredLicense.appendChild(message)
  widgetRootElement.appendChild(expiredLicense)
}

export function checkContinueConsent(parent: HTMLDivElement): void {
  // check local storage
  try {
    const item = localStorage.getItem(CONTINUE_CONSENT_KEY)
    if (item && continueIsValid(item, CONTINUE_EXPIRATION_DAYS)) {
      // license was accepted earlier
      return
    }
  } catch (e) {
    /* do nothing */
  }
  showInvalidHostMessage(parent)
}

function continueIsValid(storage: string, dayLimit: number): boolean {
  const storedDate = parseInt(storage, 10)
  const currentDate = Date.now()
  const TimeDifferenceInMs = currentDate - storedDate
  const limitDateInMs = dayLimit * 24 * 60 * 60 * 1000
  return TimeDifferenceInMs < limitDateInMs
}

/**
 * Splits the signature from the signed license object.
 */
function extractSignature(license: SignedLicenseJson): {
  licenseJson: LicenseJson
  signature: Uint8Array
} {
  // extract signature and convert
  const { signature, ...licenseJson } = license

  const hexToUint8Array = (hexString: string) => {
    const bytes = []
    for (let i = 0; i < hexString.length; i += 2) {
      bytes.push(parseInt(hexString.substr(i, 2), 16))
    }
    return new Uint8Array(bytes)
  }
  const signatureBytes = hexToUint8Array(license.signature)

  return { signature: signatureBytes, licenseJson }
}

/**
 * Checks if the license is valid wrt. the signature and whether it is valid wrt. to the given properties (expiry, domains, etc).
 */
export async function isValidLicenseKey(
  license: SignedLicenseJson | undefined
): Promise<boolean> {
  // python backend syncs empty object if no license was given
  if (!license || Object.keys(license).length === 0) {
    return false
  }

  const { licenseJson, signature } = extractSignature(license)
  let isVerifiedLicense = false
  try {
    isVerifiedLicense = await verifyMessage(licenseJson, signature)
  } catch (e) {
    console.error(
      'Cannot verify license due to unsupported crypto API in your browser'
    )
  }

  if (isVerifiedLicense) {
    // domain verification
    const domainArray = license.domains
    const domainRegex = domainArray.map((domain) => new RegExp(domain))
    const isAllowed = domainRegex.some((regexp) =>
      regexp.test(location.hostname)
    )

    // date verification
    const expiryDate = new Date(licenseJson.expiry).getTime()
    const currentDate = Date.now()

    return expiryDate > currentDate && isAllowed
  }

  return false
}
