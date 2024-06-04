import { GraphComponent, ICommand, INode } from 'yfiles'

import '../css/toolbar.css'
import '../css/loading-button.css'
import { LAYOUT_ALGORITHMS, LayoutStyle } from './algorithm'
import { LayoutSupport } from './layout-support'
import { consolidateDataObject, exportGraphML } from './graphio-utils'
import {
  mdiFullscreen,
  mdiFullscreenExit,
  mdiMapMarkerRadius,
  mdiMenuLeft,
} from '@mdi/js'
import { createIconSvg } from './utils'
import { Dialog } from './dialog'
import { isGoogleColabEnv, isVsCodeEnv } from './license-management'
import { LeafletSupport } from './map-view/leaflet-support'
import {
  startInteractiveOrganicLayout,
  stopInteractiveOrganicLayout,
} from './interactive-organic-layout'

export const YED_LIVE_URL = 'https://www.yworks.com/yed-live/'
export const DATA_EXPLORER_URL = 'https://www.yworks.com/data-explorer/' //'http://localhost:8080/'

export class Toolbar {
  private layoutCancelled = false
  private readonly rootContainer: HTMLDivElement
  private readonly primaryToolbar: HTMLDivElement
  private readonly secondaryToolbar: HTMLDivElement
  private readonly externalsToolbar: HTMLDivElement

  constructor(
    private readonly graphComponent: GraphComponent,
    private readonly widgetRootElement: HTMLElement,
    private readonly parentElement: HTMLElement,
    private readonly leafletSupport: LeafletSupport,
    private readonly hiddenNodes: Set<INode>
  ) {
    this.rootContainer = document.createElement('div')
    this.rootContainer.className = 'toolbar'

    this.primaryToolbar = document.createElement('div')
    this.primaryToolbar.className = 'toolbar-container primary elevation'

    this.secondaryToolbar = document.createElement('div')
    this.secondaryToolbar.className = 'toolbar-container secondary elevation'

    this.externalsToolbar = document.createElement('div')
    this.externalsToolbar.className = 'toolbar-container externals elevation'

    this.rootContainer.appendChild(this.primaryToolbar)
    this.rootContainer.appendChild(this.externalsToolbar)
    this.rootContainer.appendChild(this.secondaryToolbar)

    this.parentElement.appendChild(this.rootContainer)
    this.initializeToolbar()
  }

  private initializeToolbar() {
    const isGraphEmpty = this.graphComponent.graph.nodes.size === 0
    this.addIconButton(
      this.primaryToolbar,
      'Zoom In',
      'yIconZoomIn',
      (e) => {
        if (!LeafletSupport.isInMapMode(this.widgetRootElement)) {
          ICommand.INCREASE_ZOOM.execute(null, this.graphComponent)
        } else {
          // allow leaflet to listen for the toolbar buttons
          e.target!.dispatchEvent(
            new CustomEvent('yjg-zoom-in', { bubbles: true })
          )
        }
      },
      false,
      'ZoomIn'
    )
    this.addIconButton(
      this.primaryToolbar,
      'Zoom Out',
      'yIconZoomOut',
      (e) => {
        if (!LeafletSupport.isInMapMode(this.widgetRootElement)) {
          ICommand.DECREASE_ZOOM.execute(null, this.graphComponent)
        } else {
          // allow leaflet to listen for the toolbar buttons
          e.target!.dispatchEvent(
            new CustomEvent('yjg-zoom-out', { bubbles: true })
          )
        }
      },
      false,
      'ZoomOut'
    )
    this.addIconButton(
      this.primaryToolbar,
      'Fit Diagram',
      'yIconZoomFit',
      (e) => {
        if (!LeafletSupport.isInMapMode(this.widgetRootElement)) {
          ICommand.FIT_GRAPH_BOUNDS.execute(null, this.graphComponent)
        } else {
          // allow leaflet to listen for the toolbar buttons
          e.target!.dispatchEvent(
            new CustomEvent('yjg-fit-content', { bubbles: true })
          )
        }
      },
      false,
      'FitDiagram'
    )
    this.addSeparator(this.primaryToolbar)
    this.addLayoutIconMenu(this.primaryToolbar, isGraphEmpty)

    this.addIconButton(
      this.externalsToolbar,
      'Export to yEd Live',
      'yed-live-logo',
      this.openInYedLive.bind(this),
      isGraphEmpty,
      'exportYEdLive'
    )

    this.addIconButton(
      this.externalsToolbar,
      'Analyze in Data Explorer',
      'data-explorer-logo',
      this.openInDataExplorer.bind(this),
      isGraphEmpty,
      'exportDataExplorer'
    )

    const supportsFullscreen =
      document.fullscreenEnabled &&
      (!!this.widgetRootElement.requestFullscreen ||
        // @ts-ignore
        !!this.widgetRootElement.mozRequestFullScreen ||
        // @ts-ignore
        !!this.widgetRootElement.webkitRequestFullScreen ||
        // @ts-ignore
        !!this.widgetRootElement.msRequestFullscreen)

    const isFullscreenSupportingEnvironment = !isVsCodeEnv && !isGoogleColabEnv

    if (isFullscreenSupportingEnvironment && supportsFullscreen) {
      this.addMdiIconButton(
        this.secondaryToolbar,
        'Toggle Fullscreen',
        mdiFullscreen,
        this.toggleAndFit.bind(this)
      )
      this.addSeparator(this.secondaryToolbar)
    }

    this.addIconToggleButton(
      this.secondaryToolbar,
      'Toggle Sidebar',
      'yIconSidebarRight',
      true,
      this.toggleHideSidebar.bind(this)
    )
  }

  private toggleAndFit(e: Event): void {
    this.toggleFullscreen(e)
    setTimeout(() => {
      if (!LeafletSupport.isInMapMode(this.widgetRootElement)) {
        ICommand.FIT_GRAPH_BOUNDS.execute(null, this.graphComponent)
      }
    }, 30)
  }

  private openInYedLive(e: MouseEvent) {
    const button = e.target as HTMLButtonElement
    button.disabled = true

    if (isVsCodeEnv) {
      Dialog.createYedLiveDialog(
        this.widgetRootElement as HTMLDivElement,
        this.graphComponent,
        () => {
          button.disabled = false
        }
      )
    } else {
      this.openGraphIn(
        YED_LIVE_URL,
        () =>
          exportGraphML(this.graphComponent).then((graphml) => ({
            graphml,
          })),
        () => {
          button.disabled = false
        }
      )
    }
  }
  /**
   * @yjs:keep=nodes,edges
   */
  private createDataExplorerBlob(
    metaData: Record<string, unknown>,
    nodes: Record<string, unknown>[],
    edges: Record<string, unknown>[]
  ): Record<string, unknown> {
    return {
      json: {
        metaData,
        nodes,
        edges,
      },
    }
  }

  private openInDataExplorer(e: MouseEvent) {
    const button = e.target as HTMLButtonElement
    button.disabled = true

    // we cannot use this.widget.nodes() here because the current widget instance may
    // already hold a different set of items (e.g. when the same widget was used in a
    // subsequent jupyter cell)
    const nodes = this.graphComponent.graph.nodes
      .map((n) => consolidateDataObject(n.tag))
      .toArray()
    const edges = this.graphComponent.graph.edges
      .map((e) => consolidateDataObject(e.tag))
      .toArray()

    if (isVsCodeEnv) {
      Dialog.createDataExplorerDialog(
        this.widgetRootElement as HTMLDivElement,
        () =>
          Promise.resolve(
            this.createDataExplorerBlob(
              this.graphComponent.graph.tag,
              nodes,
              edges
            )
          ),
        () => {
          button.disabled = false
        }
      )
    } else {
      this.openGraphIn(
        DATA_EXPLORER_URL,
        () =>
          Promise.resolve(
            this.createDataExplorerBlob(
              this.graphComponent.graph.tag,
              nodes,
              edges
            )
          ),
        () => {
          button.disabled = false
        }
      )
    }
  }

  /**
   * @yjs:keep=origin
   */
  private openGraphIn(
    url: string,
    dataProvider: () => Promise<Record<string, unknown>>,
    cleanUp: () => void
  ) {
    // if it didn't work after some time, show an error. Maybe yEd Live was not reachable
    const failTimeout = setTimeout(() => {
      alert('Target application not answering.')
      cleanUp()
    }, 10000)

    const messageHandler = async (e: MessageEvent) => {
      // wait for page load before sending the data
      if (url.startsWith(e.origin) && e.data.indexOf('listening') !== -1) {
        window.clearTimeout(failTimeout)
        // signal an incoming graphml (creation might take some time)
        targetWindow.postMessage(
          {
            source: 'jupyter-widget',
            sending: true,
          },
          url
        )
        // send the actual graphml
        setTimeout(async () => {
          targetWindow.postMessage(
            {
              source: 'jupyter-widget',
              ...(await dataProvider()),
            },
            url
          )
        }, 500)
      }
      cleanUp()
      window.removeEventListener('message', messageHandler)
    }
    window.addEventListener('message', messageHandler)

    // try open the target app
    const targetWindow = window.open(url)!
  }

  /* View in fullscreen */
  private static openFullscreen(element: HTMLDivElement) {
    if (element.requestFullscreen) {
      // noinspection JSIgnoredPromiseFromCall
      element.requestFullscreen()
    } else {
      // @ts-ignore
      if (element.webkitRequestFullscreen) {
        /* Safari */
        // @ts-ignore
        element.webkitRequestFullscreen()
      } else {
        // @ts-ignore
        if (element.msRequestFullscreen) {
          /* IE11 */
          // @ts-ignore
          element.msRequestFullscreen()
        }
      }
    }
  }

  /* Close fullscreen */
  private static closeFullscreen() {
    // @ts-ignore
    if (document.exitFullscreen) {
      // noinspection JSIgnoredPromiseFromCall
      document.exitFullscreen()
    } else {
      // @ts-ignore
      if (document.webkitExitFullscreen) {
        /* Safari */
        // @ts-ignore
        document.webkitExitFullscreen()
      } else {
        // @ts-ignore
        if (document.msExitFullscreen) {
          /* IE11 */
          // @ts-ignore
          document.msExitFullscreen()
        }
      }
    }
  }

  public toggleFullscreen(e: Event): void {
    const elem = this.widgetRootElement as HTMLDivElement
    if (elem) {
      const button = e.currentTarget as HTMLButtonElement
      if (!document.fullscreenElement) {
        // not in fullscreen
        Toolbar.openFullscreen(elem)
        this.setButtonMdiIcon(button, mdiFullscreenExit)
      } else {
        // in fullscreen
        Toolbar.closeFullscreen()
        this.setButtonMdiIcon(button, mdiFullscreen)
      }
    }
  }

  public toggleHideSidebar(): void {
    const toolbarButton = this.secondaryToolbar.querySelector(
      '.yIconSidebarRight'
    ) as HTMLButtonElement
    toolbarButton.classList.toggle('active')
    this.widgetRootElement.classList.toggle('sidebar-right-hidden')
  }

  public closeLayoutMenu(): void {
    const layouts = this.primaryToolbar.querySelector(
      '.icon-menu.layouts'
    ) as HTMLUListElement
    layouts.classList.remove('show')
  }

  public isLayoutMenuOpen(): boolean {
    const layoutMenu = this.primaryToolbar.querySelector(
      '.icon-menu.layouts'
    ) as HTMLUListElement
    return layoutMenu.classList.contains('show')
  }

  private addTextButton(
    parent: HTMLDivElement,
    title: string,
    text: string,
    clickCallback: (e: MouseEvent) => void
  ) {
    const button = document.createElement('button')
    button.className = 'button text'
    button.title = title
    button.innerText = text
    button.addEventListener('click', clickCallback)
    parent.appendChild(button)
  }

  private addMdiIconButton(
    parent: HTMLDivElement,
    title: string,
    mdiIcon: string,
    clickCallback: (e: MouseEvent) => void
  ) {
    const button = document.createElement('button')
    button.className = 'button mdi-icon'
    button.title = title
    button.addEventListener('click', clickCallback)

    this.setButtonMdiIcon(button, mdiIcon)

    parent.appendChild(button)
  }

  private setButtonMdiIcon(btn: HTMLButtonElement, mdiIcon: string) {
    if (btn.firstElementChild) {
      btn.removeChild(btn.firstElementChild)
    }
    btn.appendChild(createIconSvg(this.widgetRootElement, mdiIcon))
  }

  private addIconButton(
    parent: HTMLDivElement,
    title: string,
    cssIconClass: string,
    clickCallback: (e: MouseEvent) => void,
    disabled = false,
    id: string | null = null
  ) {
    const button = document.createElement('button')
    button.className = `button icon ${cssIconClass}`
    button.title = title
    button.disabled = disabled
    if (id) {
      button.id = id
    }
    button.addEventListener('click', clickCallback)
    parent.appendChild(button)
  }

  private addIconToggleButton(
    parent: HTMLDivElement,
    title: string,
    cssIconClass: string,
    toggledInitially: boolean,
    clickCallback: (e: MouseEvent) => void
  ) {
    const button = document.createElement('button')
    button.className = `button toggle icon ${cssIconClass}`
    if (toggledInitially) {
      button.classList.add('active')
    }
    button.title = title
    button.addEventListener('click', (e) => {
      clickCallback(e)
    })
    parent.appendChild(button)
  }

  private addSeparator(parent: HTMLDivElement) {
    const separator = document.createElement('span')
    separator.className = 'separator'
    parent.appendChild(separator)
  }

  private addLayoutIconMenuEntry(
    layoutMenu: HTMLUListElement,
    parentList: HTMLUListElement,
    layoutStyle: LayoutStyle
  ): void {
    const layoutKey = layoutStyle.key
    const li = document.createElement('li')
    li.className = 'layout-item'
    li.title = layoutStyle.title
    li.setAttribute('data-layout-id', layoutKey)

    if (layoutKey === 'map') {
      const iconContainer = document.createElement('span')
      iconContainer.className = 'layout-mdi-icon'
      const icon = createIconSvg(this.widgetRootElement, mdiMapMarkerRadius)
      iconContainer.appendChild(icon)
      li.appendChild(iconContainer)
    }
    const title = document.createElement('span')
    title.innerText = layoutStyle.title
    li.appendChild(title)

    li.addEventListener('click', async (e) => {
      e.stopPropagation()
      layoutMenu.classList.remove('show')

      const selectedLayout = li.getAttribute('data-layout-id')!
      await this.runLayout(selectedLayout)
    })

    parentList.appendChild(li)
  }

  private addNestedLayoutIconMenu(
    layoutMenu: HTMLUListElement,
    menuItem: NestedLayoutMenu
  ): void {
    const li = document.createElement('li')
    li.title = menuItem.menuTitle
    li.innerText = menuItem.menuTitle
    li.className = 'layout-item nested-layout'

    // prevent closing of nested menu on click
    li.addEventListener('click', (ev) => ev.stopPropagation())

    const iconContainer = document.createElement('span')
    iconContainer.className = 'layout-mdi-icon'
    const icon = createIconSvg(this.widgetRootElement, mdiMenuLeft)
    iconContainer.appendChild(icon)
    li.prepend(iconContainer)

    const nestedMenu = document.createElement('ul')
    nestedMenu.className = 'icon-menu elevation layouts'
    for (const layoutStyle of menuItem.layouts) {
      this.addLayoutIconMenuEntry(layoutMenu, nestedMenu, layoutStyle)
    }
    li.appendChild(nestedMenu)
    layoutMenu.appendChild(li)
  }

  private addLayoutIconMenu(parent: HTMLDivElement, disabled = false) {
    const button = document.createElement('button')
    button.className = 'button icon layouts-menu-button'
    // add additional elements to support the loading-animation
    button.appendChild(document.createElement('span'))
    button.disabled = disabled

    const layoutMenuList = document.createElement('ul')
    layoutMenuList.className = 'icon-menu elevation layouts'

    const layoutMenuStructure = Toolbar.getLayoutMenuStructure()

    for (const menuItem of layoutMenuStructure) {
      if (isNestedLayoutMenu(menuItem)) {
        this.addNestedLayoutIconMenu(layoutMenuList, menuItem)
      } else {
        this.addLayoutIconMenuEntry(layoutMenuList, layoutMenuList, menuItem)
      }
    }

    button.addEventListener('click', async () => {
      if (button.classList.contains('yIconCancel')) {
        this.layoutCancelled = true
        await LayoutSupport.INSTANCE.cancelLayout()
      } else {
        layoutMenuList.classList.toggle('show')
      }
    })

    button.appendChild(layoutMenuList)
    parent.appendChild(button)
  }

  private toggleLeaflet(enableLeaflet: boolean): void {
    const buttons = this.widgetRootElement.querySelectorAll<HTMLButtonElement>(
      '#exportYEdLive, #exportDataExplorer'
    )
    buttons.forEach(
      (button) =>
        (button.disabled =
          enableLeaflet ?? this.graphComponent.graph.nodes.size === 0)
    )
    this.leafletSupport.toggleMapOverlay(enableLeaflet)
  }

  /**
   * Runs the given layoutKey and sets the layout-menu-button state accordingly
   */
  async runLayout(layoutKey: string): Promise<void> {
    const button = this.rootContainer.querySelector(
      '.layouts-menu-button'
    ) as HTMLButtonElement
    const layoutAlgorithm = LAYOUT_ALGORITHMS[layoutKey]

    if (!layoutAlgorithm) {
      return
    }

    this.removeLayoutButtonMdiIcon()

    if (this.getCurrentLayoutFromButton() === 'map') {
      this.toggleLeaflet(false)
    } else if (this.getCurrentLayoutFromButton() === 'interactive_organic') {
      stopInteractiveOrganicLayout(this.graphComponent)
    }

    if (layoutKey === 'map') {
      this.toggleLeaflet(true)
      this.setCurrentLayoutButton(layoutKey)
    } else {
      button.classList.add('yIconCancel', 'loading-animation')
      const oldTitle = button.title
      button.title = `Calculating ${Toolbar.getLayoutTitle(
        layoutKey
      )} layout. Press to cancel.`
      try {
        if (layoutKey === 'interactive_organic') {
          await startInteractiveOrganicLayout(
            this.graphComponent,
            this.hiddenNodes
          )
        } else {
          await LayoutSupport.INSTANCE.morphLayout(
            this.graphComponent,
            layoutAlgorithm
          )
        }
      } catch (e) {
        console.warn(e)
      } finally {
        button.classList.remove('yIconCancel', 'loading-animation')
        if (!this.layoutCancelled) {
          this.setCurrentLayoutButton(layoutKey)
        } else {
          button.title = oldTitle
          this.layoutCancelled = false
        }
      }
    }
  }

  setCurrentLayoutButton(layoutKey: string): void {
    const button = this.rootContainer.querySelector(
      '.layouts-menu-button'
    ) as HTMLButtonElement
    button.title = `Current layout: ${Toolbar.getLayoutTitle(
      layoutKey
    )}. Click for more.`
    button.setAttribute('data-current-layout', layoutKey)

    // maybe remove mdi icon to show the CSS icons on the button
    this.removeLayoutButtonMdiIcon()

    // add mdi icon instead of a CSS pseudo-element icon
    if (layoutKey === 'map') {
      const iconContainer = document.createElement('span')
      iconContainer.className = 'layout-mdi-icon'
      const icon = createIconSvg(this.widgetRootElement, mdiMapMarkerRadius)
      iconContainer.appendChild(icon)
      button.prepend(iconContainer)
    }
  }

  private removeLayoutButtonMdiIcon() {
    const button = this.rootContainer.querySelector(
      '.layouts-menu-button'
    ) as HTMLButtonElement
    if (button.firstElementChild?.classList.contains('layout-mdi-icon')) {
      button.removeChild(button.firstElementChild!)
    }
  }

  getCurrentLayoutFromButton(): string | null {
    const button = this.rootContainer.querySelector(
      '.layouts-menu-button'
    ) as HTMLButtonElement
    return button.getAttribute('data-current-layout')
  }

  private static getLayoutTitle(layoutKey: string): string {
    switch (layoutKey) {
      case 'circular':
      case 'hierarchic':
      case 'organic':
      case 'orthogonal':
      case 'radial':
      case 'tree':
        return layoutKey.substring(0, 1).toUpperCase() + layoutKey.substring(1)
      case 'orthogonal_edge_router':
        return 'Orthogonal Edge Router'
      case 'organic_edge_router':
        return 'Organic Edge Router'
      case 'interactive_organic':
        return 'Interactive Organic Layout'
      case 'map':
        return 'Geospatial Layout'
      default:
        throw new Error('Unknown Layout Key')
    }
  }

  private static getLayoutMenuStructure(): LayoutMenuStructure {
    // nest some layout algorithms in an additional menu
    const toplevelLayouts: LayoutStyle[] = []
    const organicSubmenu: NestedLayoutMenu = {
      menuTitle: 'Organic Layouts',
      layouts: [],
    }
    const routersSubmenu: NestedLayoutMenu = {
      menuTitle: 'Edge Routers',
      layouts: [],
    }

    for (const layoutKey of Object.keys(LAYOUT_ALGORITHMS)) {
      switch (layoutKey) {
        case 'organic':
        case 'interactive_organic':
          organicSubmenu.layouts.push(LAYOUT_ALGORITHMS[layoutKey])
          break
        case 'organic_edge_router':
        case 'orthogonal_edge_router':
          routersSubmenu.layouts.push(LAYOUT_ALGORITHMS[layoutKey])
          break
        default:
          toplevelLayouts.push(LAYOUT_ALGORITHMS[layoutKey])
          break
      }
    }

    return [organicSubmenu, ...toplevelLayouts, routersSubmenu]
  }
}

type LayoutMenuStructure = (LayoutStyle | NestedLayoutMenu)[]
type NestedLayoutMenu = { menuTitle: string; layouts: LayoutStyle[] }

function isNestedLayoutMenu(
  item: LayoutStyle | NestedLayoutMenu
): item is NestedLayoutMenu {
  return typeof (item as NestedLayoutMenu).menuTitle !== 'undefined'
}
