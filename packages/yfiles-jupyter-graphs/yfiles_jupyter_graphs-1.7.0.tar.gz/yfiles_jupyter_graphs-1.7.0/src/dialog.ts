import '../css/dialog.css'
import { GraphComponent } from 'yfiles'
import { exportGraphML } from './graphio-utils'
import { createIconSvg, saveToFile } from './utils'
import { mdiLaunch, mdiFile, mdiDownload, mdiCursorMove } from '@mdi/js'
import { DATA_EXPLORER_URL, YED_LIVE_URL } from './toolbar'
import { isDarkMode } from './theme-support'

export class Dialog {
  private readonly rootContainer: HTMLDivElement
  private readonly contentContainer: HTMLDivElement
  private readonly keydownListener: (e: KeyboardEvent) => void

  constructor(
    private parentElement: HTMLElement,
    private content: HTMLElement,
    private onCloseCallback: () => void = () => {
      return
    }
  ) {
    this.rootContainer = document.createElement('div')
    this.rootContainer.classList.add('dialog')
    this.rootContainer.tabIndex = -1

    this.contentContainer = document.createElement('div')
    this.contentContainer.classList.add('dialog-content')

    this.contentContainer.appendChild(content)
    this.rootContainer.appendChild(this.contentContainer)
    parentElement.appendChild(this.rootContainer)

    this.rootContainer.addEventListener('click', (e) => {
      if (e.currentTarget === e.target) {
        this.close()
      }
    })

    this.parentElement.addEventListener('keydown', (e: KeyboardEvent) => {
      e.preventDefault()
      if (e.key === 'Escape') {
        this.close()
      }
    })

    this.rootContainer.focus()
  }

  close(): void {
    this.rootContainer.remove()
    this.onCloseCallback()
  }

  private static createExportDialog(
    parentElement: HTMLElement,
    headline: string,
    exportInstructions: HTMLDivElement[],
    onCloseCallback: () => void = () => {
      return
    }
  ): Dialog {
    const content = document.createElement('div')
    content.className = 'export-dialog'
    content.innerHTML = '<p class="dialog-headline">' + headline + '</p>'

    const flexContainer = document.createElement('div')
    flexContainer.className = 'flex-container'

    exportInstructions.forEach((flexElement, index) => {
      flexElement.classList.add('flex-element')
      const stepNum = document.createElement('p')
      stepNum.className = 'step-number'
      stepNum.innerText = (index + 1).toString()

      flexElement.insertBefore(stepNum, flexElement.firstChild)

      flexContainer.appendChild(flexElement)
    })

    content.appendChild(flexContainer)
    return new Dialog(parentElement, content, onCloseCallback)
  }

  static createDataExplorerDialog(
    widgetRootElement: HTMLElement,
    dataProvider: () => Promise<Record<string, unknown>>,
    onCloseCallback: () => void = () => {
      return
    }
  ): Dialog {
    const flexLeft = document.createElement('div')
    const flexRight = document.createElement('div')
    flexRight.style.flex = '2'

    flexLeft.innerHTML = '<p>Open Data Explorer in your browser.</p>'

    this.addHrefButton(
      widgetRootElement,
      flexLeft,
      'Opens https://www.yworks.com/products/data-explorer-for-neo4j',
      'Open Data Explorer',
      mdiLaunch,
      DATA_EXPLORER_URL,
      'data-explorer-button'
    )

    flexRight.innerHTML =
      '<p>Drag and drop the file symbol below into Data Explorer.</p>'

    this.addFileDragElement(widgetRootElement, flexRight, (e) => {
      // @ts-ignore
      dataProvider().then((data) => {
        // @ts-ignore
        e.dataTransfer.setData('text/plain', JSON.stringify(data))
      })
    })

    const downloadNote = document.createElement('p')
    downloadNote.className = 'download-note'

    const downloadNodeText1 = document.createElement('span')
    downloadNodeText1.innerText = 'Alternatively,'
    downloadNote.appendChild(downloadNodeText1)

    this.addButton(
      widgetRootElement,
      downloadNote,
      'Export the graph as JSON file',
      'export',
      mdiDownload,
      async () => {
        const json = JSON.stringify(await dataProvider())
        saveToFile(json, 'yfiles-jupyter-graphs.json')
      },
      'secondary inline'
    )

    const downloadNodeText2 = document.createElement('span')
    downloadNodeText2.innerHTML = 'the file and open it in Data Explorer.'
    downloadNote.appendChild(downloadNodeText2)
    flexRight.appendChild(downloadNote)

    return this.createExportDialog(
      widgetRootElement,
      'Export to Data Explorer',
      [flexLeft, flexRight],
      onCloseCallback
    )
  }

  static createYedLiveDialog(
    widgetRootElement: HTMLElement,
    graphComponent: GraphComponent,
    onCloseCallback: () => void = () => {
      return
    }
  ): Dialog {
    const flexLeft = document.createElement('div')
    const flexRight = document.createElement('div')
    flexRight.style.flex = '2'

    flexLeft.innerHTML = '<p>Open yEd Live in your browser.</p>'

    this.addHrefButton(
      widgetRootElement,
      flexLeft,
      'Opens https://www.yworks.com/yed-live/',
      'Open yEd Live',
      mdiLaunch,
      YED_LIVE_URL,
      'yed-live-button'
    )

    flexRight.innerHTML =
      '<p>Drag and drop the file symbol below into yEd Live.</p>'

    this.addFileDragElement(widgetRootElement, flexRight, (e) => {
      exportGraphML(graphComponent).then((data) => {
        // @ts-ignore
        e.dataTransfer.setData('text/plain', data)
      })
    })

    const downloadNote = document.createElement('p')
    downloadNote.className = 'download-note'

    const downloadNodeText1 = document.createElement('span')
    downloadNodeText1.innerText = 'Alternatively,'
    downloadNote.appendChild(downloadNodeText1)

    Dialog.addButton(
      widgetRootElement,
      downloadNote,
      'Export the GraphML file',
      'export',
      mdiDownload,
      async () => {
        const graphml = await exportGraphML(graphComponent)
        saveToFile(graphml, 'yfiles-jupyter-graphs.graphml')
      },
      'secondary inline'
    )

    const downloadNodeText2 = document.createElement('span')
    downloadNodeText2.innerHTML = 'the file and open it in yEd Live.'
    downloadNote.appendChild(downloadNodeText2)
    flexRight.appendChild(downloadNote)

    return this.createExportDialog(
      widgetRootElement,
      'Export to yEd Live',
      [flexLeft, flexRight],
      onCloseCallback
    )
  }

  private static addButton(
    widgetRootElement: HTMLElement,
    parent: HTMLDivElement,
    title: string,
    text: string,
    mdiIcon: string,
    clickCallback: (e: MouseEvent) => void,
    cssClass = ''
  ) {
    const button = document.createElement('button')
    button.className = 'button ' + cssClass
    button.title = title

    const textColor = isDarkMode() ? '#ffffff' : '#242265'

    const icon = createIconSvg(widgetRootElement, mdiIcon, textColor)
    //TODO does not change color in JupyterNotebook
    icon.classList.add('mdi-icon')
    button.appendChild(icon)
    button.innerHTML += text

    button.addEventListener('click', clickCallback)
    parent.appendChild(button)
  }

  private static addHrefButton(
    widgetRootElement: HTMLElement,
    parent: HTMLDivElement,
    title: string,
    text: string,
    mdiIcon: string,
    href: string,
    cssClass = ''
  ) {
    const button = document.createElement('a') as HTMLAnchorElement
    button.href = href
    button.target = '_blank'

    button.className = 'button ' + cssClass
    button.title = title

    const icon = createIconSvg(widgetRootElement, mdiIcon, '#242265')
    icon.classList.add('mdi-icon')
    button.appendChild(icon)
    button.innerHTML += text

    parent.appendChild(button)
  }

  private static addFileDragElement(
    widgetRootElement: HTMLElement,
    parentElement: HTMLDivElement,
    setTransferData: (e: DragEvent) => void
  ) {
    const fileIcon = createIconSvg(widgetRootElement, mdiFile, '#242265')
    fileIcon.classList.add('drag-button-icon')

    const dragButton = document.createElement('div')
    dragButton.className = 'drag-button'
    dragButton.draggable = true
    dragButton.addEventListener('dragstart', (e) => {
      // @ts-ignore
      e.dataTransfer.setDragImage(
        // @ts-ignore
        fileIcon,
        fileIcon.getBoundingClientRect().width / 2,
        fileIcon.getBoundingClientRect().height / 2
      )
      // @ts-ignore
      e.dataTransfer.effectAllowed = 'copyMove'
      setTransferData(e)
    })

    const pointerIcon = createIconSvg(widgetRootElement, mdiCursorMove, '#fff')
    pointerIcon.classList.add('pointer-icon')

    dragButton.appendChild(fileIcon)
    dragButton.appendChild(pointerIcon)
    parentElement.appendChild(dragButton)

    const arrowIcon = document.createElement('div')
    arrowIcon.className = 'drag-arrow'
    arrowIcon.appendChild(
      createIconSvg(
        widgetRootElement,
        'M 3 14 V 10 H 14 V 7 L 20 12 L 14 17 V 14 H 3 Z',
        '#f9f9f9'
      )
    )
    parentElement.appendChild(arrowIcon)
  }
}
