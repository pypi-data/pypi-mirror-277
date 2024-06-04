import { isDarkMode } from './theme-support'
import {
  FilteredGraphWrapper,
  FreeEdgeLabelModel,
  FreeNodePortLocationModel,
  GraphComponent,
} from 'yfiles'

export function appendCampaign(url: string, medium: 'logo' | 'about'): string {
  // @ts-ignore
  const pluginVersion = `v${__VERSION__}`
  const campaign = 'yfiles4jupyter'
  const source = 'widget'
  return `${url}?utm_campaign=${campaign}&utm_source=${source}&utm_medium=${medium}&utm_content=${pluginVersion}`
}

export function createIconSvg(
  widgetRootElement: HTMLElement,
  pathData: string,
  fill?: string
): SVGSVGElement {
  fill = fill ?? (isDarkMode() ? '#ECEFF1' : '#52587A')
  const svgNS = 'http://www.w3.org/2000/svg'
  const svg = document.createElementNS(svgNS, 'svg') as SVGSVGElement
  svg.setAttribute('viewBox', '0 0 24 24')
  const path = document.createElementNS(svgNS, 'path') as SVGPathElement
  path.setAttribute('d', pathData)
  path.setAttribute('fill', fill)
  svg.appendChild(path)
  return svg
}

export function createMdiIconSpan(
  widgetRootElement: HTMLElement,
  mdiIcon: string,
  fill?: string,
  title?: string
): HTMLSpanElement {
  const icon = document.createElement('span')
  const svg = createIconSvg(widgetRootElement, mdiIcon, fill)
  if (title) {
    icon.title = title
  }

  icon.className = 'mdi-icon'
  icon.appendChild(svg)
  return icon
}

export function showToast(
  parent: HTMLElement,
  text: string,
  onClose?: () => void,
  floating = false,
  duration: number | null = null
): HTMLDivElement {
  const toastElement = document.createElement('div') as HTMLDivElement
  toastElement.className = `toast ${
    floating ? 'toast-floating elevation' : 'toast-bottom'
  }`

  let closeTimer = -1
  if (typeof duration === 'number') {
    closeTimer = setTimeout(() => {
      toastElement.classList.remove('show-toast')
      onClose?.()
    }, duration)
  }

  const closeBtn = document.createElement('button')
  closeBtn.title = 'Hide'
  closeBtn.className = `close yIconCancel ${floating ? 'elevation' : ''}`
  closeBtn.addEventListener('click', () => {
    clearTimeout(closeTimer)
    toastElement.classList.remove('show-toast')
    onClose?.()
  })

  const content = document.createElement('span')
  content.innerHTML = text

  toastElement.appendChild(content)
  toastElement.appendChild(closeBtn)
  parent.appendChild(toastElement)

  toastElement.classList.add('show-toast')

  return toastElement
}

export function saveToFile(fileContent: string, fileName: string): void {
  const split = fileName.split('.')
  const fileExtension = split[split.length - 1]
  const format = fileExtension.toLowerCase()

  if (
    format === 'txt' ||
    format === 'svg' ||
    format === 'graphml' ||
    format === 'pdf' ||
    format === 'png' ||
    format === 'json'
  ) {
    let mimeType = ''
    switch (format) {
      case 'png':
        mimeType = 'image/png'
        break
      case 'pdf':
        mimeType = 'text/plain; charset=x-user-defined'
        break
      case 'txt':
      default:
        mimeType = 'text/plain'
        break
      case 'svg':
        mimeType = 'image/svg+xml'
        break
      case 'graphml':
        mimeType = 'application/xml'
        break
      case 'json':
        mimeType = 'application/json'
    }

    let blob = null
    if (format === 'pdf') {
      // encode content to make transparent images work correctly
      const uint8Array = new Uint8Array(fileContent.length)
      for (let i = 0; i < fileContent.length; i++) {
        uint8Array[i] = fileContent.charCodeAt(i)
      }
      blob = new Blob([uint8Array], { type: mimeType })
    } else if (format === 'png') {
      // save as binary data
      const dataUrlParts = fileContent.split(',')
      const bString = window.atob(dataUrlParts[1])
      const byteArray = []
      for (let i = 0; i < bString.length; i++) {
        byteArray.push(bString.charCodeAt(i))
      }
      blob = new Blob([new Uint8Array(byteArray)], { type: mimeType })
    } else {
      blob = new Blob([fileContent], { type: mimeType })
    }

    // workaround for supporting non-binary data
    fileContent = URL.createObjectURL(blob)
  }

  const aElement = document.createElement('a')
  aElement.setAttribute('href', fileContent)
  aElement.setAttribute('download', fileName)
  aElement.style.display = 'none'
  document.body.appendChild(aElement)
  aElement.click()
  document.body.removeChild(aElement)

  try {
    window.URL.revokeObjectURL(fileContent)
  } catch (e) {
    /* do nothing */
  }
}

export function straightenEdges(graphComponent: GraphComponent): void {
  const filteredGraphWrapper = graphComponent.graph as FilteredGraphWrapper
  const fullGraph = filteredGraphWrapper.wrappedGraph!

  fullGraph.bends.toArray().forEach((bend) => fullGraph.remove(bend))
  fullGraph.edges.forEach((edge) => {
    const sourcePort = edge.sourcePort!
    const targetPort = edge.targetPort!
    edge.labels.forEach((label) => {
      fullGraph.setLabelLayoutParameter(
        label,
        FreeEdgeLabelModel.INSTANCE.createDefaultParameter()
      )
    })
    fullGraph.setPortLocationParameter(
      sourcePort,
      FreeNodePortLocationModel.NODE_CENTER_ANCHORED
    )
    fullGraph.setPortLocationParameter(
      targetPort,
      FreeNodePortLocationModel.NODE_CENTER_ANCHORED
    )
  })
}
