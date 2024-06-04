import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
  unpack_models,
} from '@jupyter-widgets/base'

import license from './yfiles-license.json'
import NeighborhoodView from './NeighborhoodView'

import {
  Class,
  DefaultLabelStyle,
  ExteriorLabelModel,
  FilteredGraphWrapper,
  FreeEdgeLabelModel,
  GraphBuilder,
  GraphComponent,
  GraphEditorInputMode,
  GraphItemTypes,
  GraphOverviewComponent,
  GroupNodeLabelModel,
  GroupNodeStyle,
  HorizontalTextAlignment,
  IArrow,
  IEdge,
  IEnumerable,
  IGraph,
  ILabel,
  ImageNodeStyle,
  IModelItem,
  INode,
  Insets,
  LabelCreator,
  LayoutExecutor,
  License,
  List,
  ModifierKeys,
  MouseEventRecognizers,
  MoveViewportInputMode,
  NodeSizeConstraintProvider,
  NodeStyleDecorationInstaller,
  Point,
  PolylineEdgeStyle,
  Rect,
  ScrollBarVisibility,
  ShapeNodeStyle,
  Size,
  Stroke,
  StyleDecorationZoomPolicy,
  TimeSpan,
  VerticalTextAlignment,
} from 'yfiles'

import { MODULE_NAME, MODULE_VERSION } from './version'

import type {
  ContextPaneConfig,
  Edge,
  HighlightData,
  Id,
  LayoutConfig,
  NeighborhoodConfig,
  Node as Node_,
  OverviewConfig,
  SidebarConfig,
  SignedLicenseJson,
} from './typings'
import { Highlights } from './typings'

import '../css/widget.css'
import '../css/overview.css'
import '../css/json-viewer.css'
import '../css/icons.css'
import { ElementIndicatorManager } from './highlight'
import { Toolbar } from './toolbar'
import { VueJsonViewer } from './vueJsonViewer'
import { LAYOUT_ALGORITHMS } from './algorithm'
import RenderingTypesManager from './RenderingTypesManager'
import {
  getEdgeDirection,
  getEdgeStroke,
  getEdgeStrokeThickness,
  getGroupStyling,
  getNodeLayoutProvider,
  getSelectionEdgeLabelStyleProvider,
  getSelectionEdgeStyleProvider,
  getSelectionNodeStyle,
  getTabSize,
  parseLabelObject,
  parseNodeLabelObjectParameter,
  parseStyleObject,
  svgEdgeStyleDirected,
  svgEdgeStyleUndirected,
  svgNodeStyle,
} from './graph-style-configuration'

import OverviewCanvasVisualCreator from './OverviewCanvasVisualCreator'
import { SearchBox } from './SearchBox'
import { appendCampaign, createMdiIconSpan } from './utils'
import { mdiDownload, mdiGithub } from '@mdi/js'
import {
  checkContinueConsent,
  checkLicenseConsent,
  getRemainingLicenseDays,
  initializeUpdateReminder,
  isValidHostname,
  isValidLicenseKey,
  isVsCodeEnv,
  showExpiredYfilesLicenseMessage,
} from './license-management'
import { AdjustingMouseHoverInputMode } from './AdjustingMouseHoverInputMode'
import { isDarkMode, updateThemeClass } from './theme-support'
import { configureIndicatorStyling } from './configure-hover-highlight'
import { addHeatmap } from './heatmap'
import { LeafletSupport } from './map-view/leaflet-support'
import { ContentRectViewportLimiter } from './ContentRectViewportLimiter'

// Tell the library about the license contents
License.value = license

// make sure webpack does not strip away the functionality we need for morphing
// the layouts.
Class.ensure(LayoutExecutor)

const SMALL_WIDGET_BREAKPOINT = 1200

/**
 * @yjs:keep=defaults
 */
export class GraphModel extends DOMWidgetModel {
  /**
   * @yjs:keep=deserialize
   */
  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    _nodes: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _edges: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },

    _directed: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _graph_layout: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },

    _highlight: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _neighborhood: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _sidebar: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _context_pane_mapping: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _overview: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _data_importer: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _selected_graph: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    _license: {
      // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
      deserialize: (value, manager) => unpack_models(value, manager!),
    },
    // Add any extra serializers here
  }
  static model_name = 'GraphModel'
  static model_module = MODULE_NAME
  static model_module_version = MODULE_VERSION
  static view_name = 'GraphView' // Set to null if no view
  static view_module = MODULE_NAME // Set to null if no view
  static view_module_version = MODULE_VERSION

  defaults(): any {
    return {
      ...super.defaults(),
      _model_name: GraphModel.model_name,
      _model_module: GraphModel.model_module,
      _model_module_version: GraphModel.model_module_version,
      _view_name: GraphModel.view_name,
      _view_module: GraphModel.view_module,
      _view_module_version: GraphModel.view_module_version,

      _nodes: [],
      _edges: [],

      _directed: {},
      _graph_layout: {},

      _highlight: [],
      _neighborhood: {},
      _sidebar: {},
      _context_pane_mapping: {},
      _overview: {},
      _data_importer: 'unknown',
      _selected_graph: [],
      _license: {},
      _leaflet: {},
    }
  }
}

function configureLabelUpdates<T>(labelCreator: LabelCreator<T>) {
  labelCreator.addLabelUpdatedListener((src, evt) => {
    labelCreator.updateTag(evt.graph, evt.item, evt.dataItem)
    labelCreator.updateText(evt.graph, evt.item, evt.dataItem)
    labelCreator.updateStyle(evt.graph, evt.item, evt.dataItem)
  })
}

export class GraphView extends DOMWidgetView {
  private graphComponent: GraphComponent | null | undefined
  private builder: GraphBuilder | undefined

  // noinspection JSMismatchedCollectionQueryUpdate
  private highlightManagers: ElementIndicatorManager[] = []
  private toolbar: Toolbar
  private neighborhoodView: NeighborhoodView
  private smallWidgetLayout = false
  private initializedWidgetLayout = false
  private searchBox: SearchBox
  private contextPaneConfig: ContextPaneConfig[]
  private focusInWidget = false
  private jsonViewer: VueJsonViewer

  private readonly hiddenNodes = new Set<INode>()

  get fullGraph(): IGraph {
    if (!this.graphComponent) {
      throw new Error('GraphComponent not yet initialized')
    }
    return (this.graphComponent.graph as FilteredGraphWrapper).wrappedGraph!
  }

  *nodes(): Generator<Node_, void> {
    const nodes = this.model.get('_nodes') as Node_[]
    if (nodes) {
      for (const record of nodes) {
        yield record
      }
    }
  }

  *edges(): Generator<Edge, void> {
    const edges = this.model.get('_edges') as Edge[]
    if (edges) {
      for (const record of edges) {
        yield record
      }
    }
  }

  private hideScrollMessage(): void {
    const rootElement = this.el as HTMLElement
    rootElement.classList.remove('show-scroll-hint')
  }

  private showScrollMessage(): number {
    const rootElement = this.el as HTMLElement
    rootElement.classList.add('show-scroll-hint')
    return setTimeout(() => {
      this.hideScrollMessage()
    }, 1500)
  }

  /**
   * Blocks the wheel event from reaching the given element if the widget is not focused currently.
   */
  public blockWheelInteractionWithoutFocus(element: HTMLDivElement) {
    let timeoutScrollMessage: any = null
    element.addEventListener(
      'wheel',
      (e) => {
        if (this.focusInWidget || e.ctrlKey) {
          // the overview component should handle the event, but suppress the browser's default
          // behavior
          e.preventDefault()
        } else {
          // neither GC nor overview focused, so let the browser do its thing,
          // but don't propagate the event to the overview component
          e.stopPropagation()

          // JUPY-146: vscode fix. Re-dispatch the wheel event on the widget parent to
          // correctly bubble the event to vscode
          if (isVsCodeEnv) {
            this.el.dispatchEvent(new WheelEvent('wheel', e))
          }

          if (timeoutScrollMessage !== null) {
            clearTimeout(timeoutScrollMessage)
          }
          timeoutScrollMessage = this.showScrollMessage()
        }
      },
      // tap into the event before it's processed by the overview component
      { capture: true, passive: false }
    )
  }

  /**
   * The wheel event should not register if the focus is not within our widget.
   *
   * Usually the widget is embedded in a scrollable notebook and users want to scroll the notebook primarily, so the
   * scroll event should not be consumed by our widget iff it's not focused.
   */
  private configureNoFocusBehaviour(
    graphComponent: GraphComponent,
    graphOverviewComponent: GraphOverviewComponent
  ): void {
    this.blockWheelInteractionWithoutFocus(graphComponent.div)
    this.blockWheelInteractionWithoutFocus(graphOverviewComponent.div)

    // track the bubbling focusin / focusout event to detect when the focus leaves the widget
    const rootElement = this.el as HTMLElement
    rootElement.addEventListener('focusout', () => {
      rootElement.classList.remove('focused')
      this.focusInWidget = false
    })
    rootElement.addEventListener('focusin', () => {
      rootElement.classList.add('focused')
      this.focusInWidget = true
      this.hideScrollMessage()
    })
  }

  private getLicense(): SignedLicenseJson | undefined {
    return this.getModelValue<SignedLicenseJson | undefined>('_license')
  }

  async render(): Promise<void> {
    const widgetRootElement = this.el as HTMLDivElement
    widgetRootElement.classList.add('graph-widget')

    updateThemeClass(this.el)

    const license = this.getLicense()
    const validLicenseKey = await isValidLicenseKey(license)
    if (!isValidHostname() && !validLicenseKey) {
      checkContinueConsent(widgetRootElement)
    }

    if (getRemainingLicenseDays() <= 0) {
      showExpiredYfilesLicenseMessage(widgetRootElement)
      return
    }

    const graphComponent = (this.graphComponent = new GraphComponent())
    graphComponent.viewportLimiter = new ContentRectViewportLimiter()
    // set the filtered graph as the graph to work on
    graphComponent.graph = new FilteredGraphWrapper(
      graphComponent.graph,
      (n) => !this.hiddenNodes.has(n),
      (e) => true
    )

    if (
      this.getModelValue<[]>('_nodes').some((node) => 'heat' in node) ||
      this.getModelValue<[]>('_edges').some((edge) => 'heat' in edge)
    ) {
      addHeatmap(this.graphComponent, widgetRootElement)
    }

    graphComponent.verticalScrollBarPolicy =
      ScrollBarVisibility.AS_NEEDED_DYNAMIC
    graphComponent.horizontalScrollBarPolicy =
      ScrollBarVisibility.AS_NEEDED_DYNAMIC

    // consider the floating toolbar on the top
    graphComponent.contentMargins = new Insets(10, 10, 70, 10)
    graphComponent.maximumZoom = 4
    const graphOverviewComponent = new GraphOverviewComponent(graphComponent)

    this.configureNoFocusBehaviour(graphComponent, graphOverviewComponent)

    // use canvas with circular overview styles
    graphOverviewComponent.graphVisualCreator = new OverviewCanvasVisualCreator(
      graphComponent.graph,
      isDarkMode()
    )

    this.setupLevelOfDetailRendering(graphComponent)
    this.setupInteractions(graphComponent)
    this.initializeSelectionStyles(graphComponent)

    // make sure that the group node label is not clipped by the group node size
    graphComponent.graph.decorator.nodeDecorator.sizeConstraintProviderDecorator.setImplementationWrapper(
      (node) => graphComponent.graph.isGroupNode(node),
      (groupNode, provider) => {
        const gns = groupNode?.style
        if (!groupNode || !(gns instanceof GroupNodeStyle)) {
          return null
        }

        const tabSize = getTabSize(groupNode, gns)
        const origMinSize = provider!.getMinimumSize(groupNode)
        const minSize = new Size(
          Math.max(origMinSize.width, tabSize.width),
          Math.max(origMinSize.height, tabSize.height)
        )

        return new NodeSizeConstraintProvider(
          minSize,
          provider!.getMinimumSize(groupNode),
          provider!.getMinimumEnclosedArea(groupNode)
        )
      }
    )

    this.builder = this.createGraphBuilder()
    this.builder.buildGraph()

    this.addGraphMetaData(graphComponent.graph)

    this.mountComponent(
      widgetRootElement,
      graphComponent,
      graphOverviewComponent
    )

    this.initializeHighlights()

    setTimeout(async () => {
      if (!LeafletSupport.isInMapMode(widgetRootElement)) {
        // fit initially, the layout may take some time
        await graphComponent.fitGraphBounds()
      }
      await this.morphSelectedLayout()
    }, 20)

    // TODO: should the widget be updated by *downstream* jupyter cells?!
    // this.model.on('change:_nodes', this.data_changed, this)
    // this.model.on('change:_edges', this.data_changed, this)
    //
    // this.model.on('change:_highlight', this.highlight_changed, this)
  }

  private initializeLayoutMenu() {
    // sync the state with the incoming state of the python API
    let initialLayout = 'organic'
    const layoutConfig = this.model.get('_graph_layout') as LayoutConfig
    if (layoutConfig && typeof layoutConfig.algorithm !== 'undefined') {
      const userLayout = layoutConfig.algorithm
      if (LAYOUT_ALGORITHMS[userLayout]) {
        // incoming layout is defined and available
        initialLayout = userLayout
      }
    }

    // pre-select the respective option in the dropdown
    this.toolbar.setCurrentLayoutButton(initialLayout)

    // register close listener
    this.graphComponent!.div.addEventListener('mousedown', (e) => {
      if (this.toolbar.isLayoutMenuOpen()) {
        this.toolbar.closeLayoutMenu()
        // prevent reaching the GraphComponent in this case
        e.stopImmediatePropagation()
      }
    })
  }

  morphSelectedLayout(): Promise<void> {
    const layout = this.toolbar.getCurrentLayoutFromButton() || 'organic'
    return this.toolbar.runLayout(layout)
  }

  /**
   * @yjs:keep=properties,start,end,id
   */
  setSelectionPython(): void {
    // creates a return data object in accordance to the documentation
    function createPythonDataObject(
      item: INode | IEdge
    ): Record<string, unknown> {
      const data = item.tag
      if (item instanceof INode) {
        return { id: data.id, properties: data.properties }
      }
      return {
        id: data.id,
        start: data.start,
        end: data.end,
        properties: data.properties,
      }
    }

    const selectedNodeData = this.graphComponent!.selection.selectedNodes.map(
      createPythonDataObject
    ).toArray()
    const selectedEdgeData = this.graphComponent!.selection.selectedEdges.map(
      createPythonDataObject
    ).toArray()
    this.model.set('_selected_graph', [selectedNodeData, selectedEdgeData])
    this.model.save_changes()
  }

  private static initializeScrollMessage(parent: HTMLDivElement): void {
    const scrollMessage = document.createElement('div') as HTMLDivElement
    scrollMessage.className = 'scroll-message'
    scrollMessage.id = 'scroll-message'
    const scrollSpanMessage = document.createElement('span')
    scrollSpanMessage.style.verticalAlign = 'middle'
    scrollSpanMessage.innerText =
      'To zoom the graph, focus the widget or use CTRL + scroll'
    scrollMessage.appendChild(scrollSpanMessage)
    parent.appendChild(scrollMessage)
  }

  private mountComponent(
    widgetRootElement: HTMLDivElement,
    graphComponent: GraphComponent,
    graphOverviewComponent: GraphOverviewComponent
  ) {
    this.initializeResizeObserver()
    this.contextPaneConfig = this.getContextPaneConfig()

    const { mainContainer, gcContainer } = GraphView.initializeGraphComponent(
      graphComponent,
      widgetRootElement
    )
    this.jsonViewer = new VueJsonViewer()
    this.initializeContextContainer(widgetRootElement, graphComponent)
    this.initializeGraphOverview(graphOverviewComponent, mainContainer)

    const leafletSupport = new LeafletSupport(
      graphComponent,
      widgetRootElement,
      this.hiddenNodes
    )

    this.toolbar = new Toolbar(
      graphComponent,
      widgetRootElement,
      gcContainer,
      leafletSupport,
      this.hiddenNodes
    )
    this.initializeLayoutMenu()

    const neighborhoodConfig = this.getNeighborhoodConfig()
    if (typeof neighborhoodConfig.maxDistance !== 'undefined') {
      this.neighborhoodView.maxDistance = neighborhoodConfig.maxDistance
    }
    neighborhoodConfig.selectedNodes.forEach((node) => {
      graphComponent.selection.setSelected(node, true)
    })

    const sidebarConfig = this.getSidebarConfig()
    if (!sidebarConfig.enabled) {
      this.toolbar.toggleHideSidebar()
    }

    checkLicenseConsent(gcContainer)
    initializeUpdateReminder(mainContainer)

    GraphView.initializeScrollMessage(widgetRootElement)

    // show about initially
    this.showContextPane(widgetRootElement, sidebarConfig.start_with)

    // enable transition of container width for smoother responsiveness
    setTimeout(() => {
      mainContainer.classList.add('animate-responsiveness')
    }, 500)
  }

  private addContextTabButton(
    graphWidget: HTMLElement,
    tabRow: HTMLElement,
    id: string,
    title?: string,
    tooltip?: string,
    css?: string
  ) {
    const tab = document.createElement('div')
    tab.className = 'tab-button'
    tab.tabIndex = -1 // make it focusable to not lose focus in widget when clicking
    if (css) {
      tab.classList.add(css)
    }
    if (title) {
      tab.innerText = title
    }
    if (tooltip) {
      tab.title = tooltip
    }
    tab.setAttribute('data-btn-pane-id', id)

    tab.addEventListener('click', () => {
      this.showContextPane(graphWidget, id)
    })

    tabRow.appendChild(tab)
  }

  private initializeContextContainer(
    graphWidget: HTMLElement,
    graphComponent: GraphComponent
  ) {
    const contextContainer = document.createElement('div')
    contextContainer.className = 'context-container'

    // add tabs
    const tabRow = document.createElement('div')
    tabRow.className = 'context-tabs'
    this.addContextTabButton(
      graphWidget,
      tabRow,
      this.contextPaneConfig[0].id,
      this.contextPaneConfig[0].title,
      'Inspect the local neighborhood of selected nodes'
    )
    this.addContextTabButton(
      graphWidget,
      tabRow,
      this.contextPaneConfig[1].id,
      this.contextPaneConfig[1].title,
      'Inspect the data of selected nodes'
    )
    this.addContextTabButton(
      graphWidget,
      tabRow,
      this.contextPaneConfig[2].id,
      this.contextPaneConfig[2].title,
      'Search diagram items'
    )
    this.addContextTabButton(
      graphWidget,
      tabRow,
      this.contextPaneConfig[3].id,
      this.contextPaneConfig[3].title,
      'About Us',
      'about'
    )
    contextContainer.appendChild(tabRow)

    // add context panes
    contextContainer.appendChild(
      this.createNeighborhoodPane(graphComponent, this.contextPaneConfig[0].id)
    )
    contextContainer.appendChild(
      this.createDataPane(this.contextPaneConfig[1].id)
    )
    contextContainer.appendChild(
      this.createSearchPane(graphComponent, this.contextPaneConfig[2].id)
    )
    contextContainer.appendChild(
      this.createAboutPane(this.contextPaneConfig[3].id)
    )

    graphWidget.appendChild(contextContainer)

    // init state on context-views
    this.onSelectionChanged()
  }

  private createSearchPane(
    graphComponent: GraphComponent,
    id: string
  ): HTMLDivElement {
    const root = document.createElement('div')
    root.className = 'context-pane'
    root.tabIndex = -1 // make it focusable to not lose focus in widget when clicking
    root.setAttribute('data-context-pane-id', id)
    this.searchBox = new SearchBox(this.el, root, graphComponent)

    return root
  }

  private createNeighborhoodPane(graphComponent: GraphComponent, id: string) {
    const neighborhoodPane = document.createElement('div')
    neighborhoodPane.className = 'context-pane'
    neighborhoodPane.tabIndex = -1 // make it focusable to not lose focus in widget when clicking
    neighborhoodPane.setAttribute('data-context-pane-id', id)

    const neighborhoodContainer = document.createElement('div')
    neighborhoodContainer.className = 'neighborhood-graph-container'
    neighborhoodPane.appendChild(neighborhoodContainer)

    const noSelectionInfo = document.createElement('div')
    noSelectionInfo.innerText =
      'Please select a node or an edge in the diagram to inspect its neighborhood.'
    noSelectionInfo.className = 'no-selection'
    noSelectionInfo.style.opacity = '1'
    neighborhoodPane.appendChild(noSelectionInfo)

    this.initializeNeighborhoodView(neighborhoodContainer, graphComponent)
    return neighborhoodPane
  }

  /**
   * Initialize neighborhood view.
   */
  private initializeNeighborhoodView(
    neighborhoodPane: HTMLDivElement,
    graphComponent: GraphComponent
  ) {
    const neighborhoodView = new NeighborhoodView(neighborhoodPane, this)
    neighborhoodView.graphComponent = graphComponent
    neighborhoodView.useSelection = true
    // mirror navigation in the neighborhood view to the graph component
    neighborhoodView.clickCallback = (item: INode | IEdge): void => {
      graphComponent.currentItem = item
      graphComponent.selection.clear()
      graphComponent.selection.setSelected(item, true)
      const nodes = new List(graphComponent.selection.selectedNodes).concat(
        graphComponent.selection.selectedEdges
      )
      this.highlightGraphItems(graphComponent, nodes)
      // Zoom to node or edge...
      this.panToItem(item)
    }
    this.neighborhoodView = neighborhoodView

    return neighborhoodView
  }

  /**
   * Pans to the given item iff the item is not fully visible.
   */
  private panToItem(
    item: INode | IEdge,
    margins = new Insets(10)
  ): Promise<void> {
    const graphComponent = this.graphComponent!

    let targetBounds: Rect
    if (item instanceof INode) {
      targetBounds = item.layout.toRect().getEnlarged(margins)
    } else {
      targetBounds = Rect.add(
        item.sourceNode!.layout.toRect(),
        item.targetNode!.layout.toRect()
      ).getEnlarged(margins)
    }
    // ... if the element is outside the viewport.
    const viewport = graphComponent.viewport
    if (
      !viewport.contains(targetBounds.topLeft) ||
      !viewport.contains(targetBounds.bottomRight)
    ) {
      return graphComponent.zoomToAnimated(
        targetBounds.center,
        graphComponent.zoom
      )
    }
    return Promise.resolve()
  }

  /**
   * Helper method to highlight given graph items.
   */
  private highlightGraphItems(
    graphComponent: GraphComponent,
    items: IEnumerable<INode | IEdge>
  ): void {
    const manager = graphComponent.highlightIndicatorManager
    manager.clearHighlights()
    items.forEach((item) => {
      manager.addHighlight(item)
      if (item instanceof IEdge) {
        item.labels.forEach((label) => manager.addHighlight(label))
      }
    })
  }

  /**
   * Helper method to initialize the highlighting of the graph.
   */
  private initializeSelectionStyles(graphComponent: GraphComponent): void {
    const decorator = graphComponent.graph.decorator

    decorator.nodeDecorator.highlightDecorator.setFactory((node) => {
      return new NodeStyleDecorationInstaller({
        margins: 5,
        zoomPolicy: StyleDecorationZoomPolicy.MIXED,
        nodeStyle: getSelectionNodeStyle(node),
      })
    })

    decorator.edgeDecorator.highlightDecorator.setFactory(
      getSelectionEdgeStyleProvider(this.getDirectedValue())
    )

    decorator.labelDecorator.highlightDecorator.setFactory(
      getSelectionEdgeLabelStyleProvider()
    )
  }

  // noinspection JSMethodCanBeStatic
  private createDataPane(id: string): HTMLDivElement {
    const dataPane = document.createElement('div')
    dataPane.className = 'context-pane'
    dataPane.tabIndex = -1 // make it focusable to not lose focus in widget when clicking
    dataPane.setAttribute('data-context-pane-id', id)
    return dataPane
  }

  private createAboutPane(id: string): HTMLDivElement {
    const root = document.createElement('div')
    root.className = 'context-pane'
    root.tabIndex = -1 // make it focusable to not lose focus in widget when clicking
    root.setAttribute('data-context-pane-id', id)

    const about = document.createElement('div')
    about.className = 'about-content'

    const isDarkTheme = isDarkMode()

    const logo = new Image()
    // loading or inlining of imported SVGs fails for the labextension plugin, even when providing the respective webpack rules
    const jupyterGraphsLogoBlue =
      "data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg id='a' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 398.14 109.18'%3E%3Cg id='b'%3E%3Cpath d='M0,37.41l.09,19.36c.04,9.83,5.33,18.89,13.87,23.77l16.81,9.6c8.54,4.88,19.03,4.83,27.52-.13l16.72-9.76c8.49-4.96,13.69-14.06,13.65-23.9l-.09-19.36c-.05-9.83-5.33-18.89-13.87-23.77L57.89,3.62c-8.54-4.88-19.03-4.83-27.52,.13L13.65,13.51C5.16,18.46-.05,27.57,0,37.41' fill='%23242265'/%3E%3Cg id='c'%3E%3Cg%3E%3Cpath d='M42.96,64.19c-.36,1.68-1.19,3.18-2.05,4.66-1.58,2.73-3.04,6.12-.89,9.02,1.71,2.31,5.08,2.85,7.48,1.19,2.92-2.03,2.76-5.81,1.24-8.65-.78-1.45-1.7-2.81-2.33-4.34-.69-1.67-.93-3.42-.97-5.22,0-.36,0-.73-.01-1.09h-2.11c0,1.48-.05,2.99-.36,4.43Z' fill='%23fff'/%3E%3Cpath d='M42.96,29.53c-.36-1.68-1.19-3.18-2.05-4.66-1.58-2.73-3.04-6.12-.89-9.02,1.71-2.31,5.08-2.85,7.48-1.19,2.92,2.03,2.76,5.81,1.24,8.65-.78,1.45-1.7,2.81-2.33,4.34-.69,1.67-.93,3.42-.97,5.22,0,.36,0,.73-.01,1.09h-2.11c0-1.48-.05-2.99-.36-4.43Z' fill='%23fff'/%3E%3Crect x='43.32' y='33.66' width='2.11' height='26.44' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M30.07,56.75c-1.27,1.15-2.16,2.63-3.01,4.1-1.57,2.73-3.78,5.69-7.37,5.28-2.86-.32-5.01-2.97-4.77-5.88,.3-3.55,3.65-5.3,6.87-5.4,1.64-.05,3.28,.06,4.92-.15,1.8-.24,3.43-.9,5.01-1.77,.32-.18,.63-.35,.95-.53l1.05,1.83c-1.29,.73-2.56,1.54-3.65,2.53Z' fill='%23fff'/%3E%3Cpath d='M60.09,39.42c1.63-.53,3.35-.56,5.06-.55,3.15,0,6.82-.43,8.26-3.74,1.15-2.64-.07-5.83-2.71-7.07-3.22-1.52-6.41,.51-8.11,3.25-.87,1.4-1.58,2.87-2.59,4.19-1.1,1.44-2.5,2.52-4.04,3.45-.31,.19-.62,.37-.94,.55l1.05,1.83c1.28-.75,2.62-1.45,4.01-1.9Z' fill='%23fff'/%3E%3Crect x='43.3' y='33.65' width='2.11' height='26.44' transform='translate(25.94 108.72) rotate(-120)' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M60.09,54.3c1.63,.53,3.35,.56,5.06,.55,3.15,0,6.82,.43,8.26,3.74,1.15,2.64-.07,5.83-2.71,7.07-3.22,1.52-6.41-.51-8.11-3.25-.87-1.4-1.58-2.87-2.59-4.19-1.1-1.44-2.5-2.52-4.04-3.45-.31-.19-.62-.37-.94-.55l1.05-1.83c1.28,.75,2.62,1.45,4.01,1.9Z' fill='%23fff'/%3E%3Cpath d='M30.07,36.97c-1.27-1.15-2.16-2.63-3.01-4.1-1.57-2.73-3.78-5.69-7.37-5.28-2.86,.32-5.01,2.97-4.77,5.88,.3,3.55,3.65,5.3,6.87,5.4,1.64,.05,3.28-.06,4.92,.15,1.8,.24,3.43,.9,5.01,1.77,.32,.18,.63,.35,.95,.53l1.05-1.83c-1.29-.73-2.56-1.54-3.65-2.53Z' fill='%23fff'/%3E%3Crect x='43.34' y='33.65' width='2.11' height='26.44' transform='translate(107.18 31.86) rotate(120)' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M66.99,50.35c-.36,1.68-1.19,3.18-2.05,4.66-1.58,2.73-3.04,6.12-.89,9.02,1.71,2.31,5.08,2.85,7.48,1.19,2.92-2.03,2.76-5.81,1.24-8.65-.78-1.45-1.7-2.81-2.33-4.34-.69-1.67-.93-3.42-.97-5.22,0-.36,0-.73-.01-1.09h-2.11c0,1.48-.05,2.99-.36,4.43Z' fill='%23fff'/%3E%3Cpath d='M66.99,43.37c-.36-1.68-1.19-3.18-2.05-4.66-1.58-2.73-3.04-6.12-.89-9.02,1.71-2.31,5.08-2.85,7.48-1.19,2.92,2.03,2.76,5.81,1.24,8.65-.78,1.45-1.7,2.81-2.33,4.34-.69,1.67-.93,3.42-.97,5.22,0,.36,0,.73-.01,1.09h-2.11c0-1.48-.05-2.99-.36-4.43Z' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M18.87,50.35c-.36,1.68-1.19,3.18-2.05,4.66-1.58,2.73-3.04,6.12-.89,9.02,1.71,2.31,5.08,2.85,7.48,1.19,2.92-2.03,2.76-5.81,1.24-8.65-.78-1.45-1.7-2.81-2.33-4.34-.69-1.67-.93-3.42-.97-5.22,0-.36,0-.73-.01-1.09h-2.11c0,1.48-.05,2.99-.36,4.43Z' fill='%23fff'/%3E%3Cpath d='M18.87,43.37c-.36-1.68-1.19-3.18-2.05-4.66-1.58-2.73-3.04-6.12-.89-9.02,1.71-2.31,5.08-2.85,7.48-1.19,2.92,2.03,2.76,5.81,1.24,8.65-.78,1.45-1.7,2.81-2.33,4.34-.69,1.67-.93,3.42-.97,5.22,0,.36,0,.73-.01,1.09h-2.11c0-1.48-.05-2.99-.36-4.43Z' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M30.02,29.06c-1.27,1.15-2.16,2.63-3.01,4.1-1.57,2.73-3.78,5.69-7.37,5.28-2.86-.32-5.01-2.97-4.77-5.88,.3-3.55,3.65-5.3,6.87-5.4,1.64-.05,3.28,.06,4.92-.15,1.8-.24,3.43-.9,5.01-1.77,.32-.18,.63-.35,.95-.53l1.05,1.83c-1.29,.73-2.56,1.54-3.65,2.53Z' fill='%23fff'/%3E%3Cpath d='M36.06,25.58c1.63-.53,3.35-.56,5.06-.55,3.15,0,6.82-.43,8.26-3.74,1.15-2.64-.07-5.83-2.71-7.07-3.22-1.52-6.41,.51-8.11,3.25-.87,1.4-1.58,2.87-2.59,4.19-1.1,1.44-2.5,2.52-4.04,3.45-.31,.19-.62,.37-.94,.55l1.05,1.83c1.28-.75,2.62-1.45,4.01-1.9Z' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M54.1,70.6c-1.27,1.15-2.16,2.63-3.01,4.1-1.57,2.73-3.78,5.69-7.37,5.28-2.86-.32-5.01-2.97-4.77-5.88,.3-3.55,3.65-5.3,6.87-5.4,1.64-.05,3.28,.06,4.92-.15,1.8-.24,3.43-.9,5.01-1.77,.32-.18,.63-.35,.95-.53l1.05,1.83c-1.29,.73-2.56,1.54-3.65,2.53Z' fill='%23fff'/%3E%3Cpath d='M60.14,67.12c1.63-.53,3.35-.56,5.06-.55,3.15,0,6.82-.43,8.26-3.74,1.15-2.64-.07-5.83-2.71-7.07-3.22-1.52-6.41,.51-8.11,3.25-.87,1.4-1.58,2.87-2.59,4.19-1.1,1.44-2.5,2.52-4.04,3.45-.31,.19-.62,.37-.94,.55l1.05,1.83c1.28-.75,2.62-1.45,4.01-1.9Z' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M58.73,29.06c1.27,1.15,2.16,2.63,3.01,4.1,1.57,2.73,3.78,5.69,7.37,5.28,2.86-.32,5.01-2.97,4.77-5.88-.3-3.55-3.65-5.3-6.87-5.4-1.64-.05-3.28,.06-4.92-.15-1.8-.24-3.43-.9-5.01-1.77-.32-.18-.63-.35-.95-.53l-1.05,1.83c1.29,.73,2.56,1.54,3.65,2.53Z' fill='%23fff'/%3E%3Cpath d='M52.69,25.58c-1.63-.53-3.35-.56-5.06-.55-3.15,0-6.82-.43-8.26-3.74-1.15-2.64,.07-5.83,2.71-7.07,3.22-1.52,6.41,.51,8.11,3.25,.87,1.4,1.58,2.87,2.59,4.19,1.1,1.44,2.5,2.52,4.04,3.45,.31,.19,.62,.37,.94,.55l-1.05,1.83c-1.28-.75-2.62-1.45-4.01-1.9Z' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M34.64,70.6c1.27,1.15,2.16,2.63,3.01,4.1,1.57,2.73,3.78,5.69,7.37,5.28,2.86-.32,5.01-2.97,4.77-5.88-.3-3.55-3.65-5.3-6.87-5.4-1.64-.05-3.28,.06-4.92-.15-1.8-.24-3.43-.9-5.01-1.77-.32-.18-.63-.35-.95-.53l-1.05,1.83c1.29,.73,2.56,1.54,3.65,2.53Z' fill='%23fff'/%3E%3Cpath d='M28.6,67.12c-1.63-.53-3.35-.56-5.06-.55-3.15,0-6.82-.43-8.26-3.74-1.15-2.64,.07-5.83,2.71-7.07,3.22-1.52,6.41,.51,8.11,3.25,.87,1.4,1.58,2.87,2.59,4.19,1.1,1.44,2.5,2.52,4.04,3.45,.31,.19,.62,.37,.94,.55l-1.05,1.83c-1.28-.75-2.62-1.45-4.01-1.9Z' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cg%3E%3Cpath d='M61.95,41.28c.53-1.63,.56-3.35,.55-5.06,0-3.15,.43-6.82,3.74-8.26,2.64-1.15,5.83,.07,7.07,2.71,1.52,3.22-.51,6.41-3.25,8.11-1.4,.87-2.87,1.58-4.19,2.59-1.44,1.1-2.52,2.5-3.45,4.04-.19,.31-.37,.62-.55,.94l-1.83-1.05c.75-1.28,1.45-2.62,1.9-4.01Z' fill='%23fff'/%3E%3Cpath d='M48.36,64.86c-1.15,1.27-2.63,2.16-4.1,3.01-2.73,1.57-5.69,3.78-5.28,7.37,.32,2.86,2.97,5.01,5.88,4.77,3.55-.3,5.3-3.65,5.4-6.87,.05-1.64-.06-3.28,.15-4.92,.24-1.8,.9-3.43,1.77-5.01,.18-.32,.35-.63,.53-.95l-1.83-1.05c-.73,1.29-1.54,2.56-2.53,3.65Z' fill='%23fff'/%3E%3Crect x='55.82' y='42.51' width='2.11' height='20.88' transform='translate(34.09 -21.34) rotate(30)' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M26.79,41.28c-.53-1.63-.56-3.35-.55-5.06,0-3.15-.43-6.82-3.74-8.26-2.64-1.15-5.83,.07-7.07,2.71-1.52,3.22,.51,6.41,3.25,8.11,1.4,.87,2.87,1.58,4.19,2.59,1.44,1.1,2.52,2.5,3.45,4.04,.19,.31,.37,.62,.55,.94l1.83-1.05c-.75-1.28-1.45-2.62-1.9-4.01Z' fill='%23fff'/%3E%3Cpath d='M40.39,64.86c1.15,1.27,2.63,2.16,4.1,3.01,2.73,1.57,5.69,3.78,5.28,7.37-.32,2.86-2.97,5.01-5.88,4.77-3.55-.3-5.3-3.65-5.4-6.87-.05-1.64,.06-3.28-.15-4.92-.24-1.8-.9-3.43-1.77-5.01-.18-.32-.35-.63-.53-.95l1.83-1.05c.73,1.29,1.54,2.56,2.53,3.65Z' fill='%23fff'/%3E%3Crect x='30.82' y='42.51' width='2.11' height='20.88' transform='translate(85.95 82.86) rotate(150)' fill='%23fff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M57.96,34.4c1.68,.36,3.18,1.19,4.66,2.05,2.73,1.58,6.12,3.04,9.02,.89,2.31-1.71,2.85-5.08,1.19-7.48-2.03-2.92-5.81-2.76-8.65-1.24-1.45,.78-2.81,1.7-4.34,2.33-1.67,.69-3.42,.93-5.22,.97-.36,0-.73,0-1.09,.01v2.11c1.48,0,2.99,.05,4.43,.36Z' fill='%23fff'/%3E%3Cpath d='M30.75,34.39c-1.68,.36-3.18,1.19-4.66,2.05-2.73,1.58-6.12,3.04-9.02,.89-2.31-1.71-2.85-5.08-1.19-7.48,2.03-2.92,5.81-2.76,8.65-1.24,1.45,.78,2.81,1.7,4.34,2.33,1.67,.69,3.42,.93,5.22,.97,.36,0,.73,0,1.09,.01v2.11c-1.48,0-2.99,.05-4.43,.36Z' fill='%23fff'/%3E%3Crect x='44.26' y='22.53' width='2.11' height='20.88' transform='translate(12.35 78.29) rotate(-90)' fill='%23fff'/%3E%3C/g%3E%3C/g%3E%3Ccircle cx='44.37' cy='19.13' r='5.43' fill='%23fff'/%3E%3Ccircle cx='44.37' cy='74.59' r='5.43' fill='%23fff'/%3E%3Ccircle cx='68.39' cy='32.99' r='5.43' fill='%23fff'/%3E%3Ccircle cx='20.36' cy='60.72' r='5.43' fill='%23fff'/%3E%3Ccircle cx='20.36' cy='32.99' r='5.43' fill='%23fff'/%3E%3Ccircle cx='68.39' cy='60.72' r='5.43' fill='%23fff'/%3E%3C/g%3E%3Cg id='d'%3E%3Cg%3E%3Cpath d='M130.81,37.81v.16l-13.94,35.13h-6.15v-.11l5.25-12.14-10.12-22.89v-.16h6.25l5.03,12.08c.58,1.43,1.11,2.86,1.59,4.61,.48-1.75,.95-3.18,1.43-4.61l4.61-12.08h6.04Z' fill='%23242265'/%3E%3Cpath d='M135.69,25.41h22.52v5.78h-16.27v10.39h14.57v5.62h-14.57v14.25h-6.25V25.41Z' fill='%23242265'/%3E%3Cpath d='M162.72,29.44c0-1.91,1.38-3.44,3.6-3.44s3.6,1.54,3.6,3.5-1.43,3.39-3.6,3.39-3.6-1.54-3.6-3.44Zm.69,8.37h5.78v23.63h-5.78v-23.63Z' fill='%23242265'/%3E%3Cpath d='M175.97,23.29h5.78l.05,38.15h-5.83V23.29Z' fill='%23242265'/%3E%3Cpath d='M210.04,48.78c0,.85-.11,1.8-.21,2.76h-16.96c.74,3.82,3.71,5.83,7.53,5.83,2.7,0,4.61-.79,6.25-2.23l2.44,3.71c-2.7,2.17-5.56,3.29-9.22,3.29-7.58,0-12.77-5.14-12.77-12.56,0-6.94,5.03-12.4,12.19-12.4,6.68,0,10.76,4.5,10.76,11.61Zm-17.12-1.17h11.66c-.16-3.76-2.38-5.72-5.41-5.72s-5.62,2.07-6.25,5.72Z' fill='%23242265'/%3E%3Cpath d='M213.39,59.38l2.28-4.08c2.01,1.27,4.24,1.96,6.47,1.96s3.5-.95,3.5-2.44c0-1.75-2.23-2.6-4.56-3.5-3.76-1.43-6.68-3.39-6.68-7.26,0-4.35,3.87-6.62,8.37-6.62,2.7,0,5.19,.64,7.74,2.12l-2.01,3.87c-1.75-.9-3.66-1.38-5.25-1.38-1.8,0-3.34,.53-3.34,2.01s1.75,2.44,4.29,3.34c4.13,1.54,7.1,3.5,7.1,7.42,0,4.4-3.55,7.15-8.74,7.15-3.5,0-6.41-.85-9.17-2.6Z' fill='%23242265'/%3E%3Cpath d='M271.74,37.81v24.59c0,7.58-5.14,11.34-12.4,11.34-4.34,0-7.79-1.22-10.7-3.6l2.23-4.35c2.17,1.75,4.77,2.76,8,2.76,4.29,0,7.05-2.01,7.05-6.04,0-1.22,.05-2.54,.11-3.87-2.07,2.17-4.88,3.23-7.84,3.23-6.73,0-11.34-5.09-11.34-12.29s4.61-12.35,11.23-12.35c3.55,0,6.68,1.32,8.69,4.03l1.17-3.44h3.82Zm-5.56,11.76c0-4.19-2.38-7.31-6.78-7.31s-6.68,3.02-6.68,7.31,2.54,7.31,6.62,7.31c4.45,0,6.84-3.13,6.84-7.31Z' fill='%23242265'/%3E%3Cpath d='M294.47,38.29l-1.48,4.88c-.9-.32-1.85-.53-3.07-.53-3.34,0-5.62,2.17-5.62,5.94v12.88h-5.78v-23.63h3.92l1.11,3.5c1.38-2.65,3.76-4.03,6.84-4.03,1.64,0,2.97,.37,4.08,1.01Z' fill='%23242265'/%3E%3Cpath d='M317.37,46.18v15.26h-3.87l-1.06-3.55c-1.75,2.49-4.56,4.03-8.43,4.03-4.34,0-7.42-2.44-7.42-6.62,0-5.4,4.77-8.37,11.98-8.37,1.22,0,2.12,.05,2.97,.11v-1.06c0-2.44-1.8-3.66-4.82-3.66-2.33,0-4.93,.74-7.37,1.91l-1.64-4.4c3.5-1.59,6.73-2.44,9.91-2.44,6.04,0,9.75,3.07,9.75,8.8Zm-5.67,4.61c-.95-.11-1.7-.16-2.76-.16-4.19,0-6.62,1.48-6.62,4.08,0,1.85,1.27,2.86,3.39,2.86,3.39,0,5.88-2.49,5.99-6.78Z' fill='%23242265'/%3E%3Cpath d='M348.74,49.52c0,7.37-4.72,12.51-11.29,12.51-3.29,0-6.04-1.27-7.95-3.29,.11,1.64,.11,3.55,.11,5.62v8.74h-5.78V37.81h3.92l1.11,3.6c1.96-2.6,4.93-4.19,8.58-4.19,6.52,0,11.29,5.19,11.29,12.29Zm-5.88,.16c0-4.4-2.65-7.37-6.62-7.37s-6.84,2.91-6.84,7.26,2.81,7.42,6.84,7.42,6.62-3.02,6.62-7.31Z' fill='%23242265'/%3E%3Cpath d='M375.51,46.61v14.84h-5.78v-14.36c0-2.86-1.22-4.72-4.08-4.72-3.76,0-5.72,3.13-5.72,6.89v12.19h-5.78V23.29h5.78v14.1c0,1.11,0,2.17-.05,3.6,1.48-2.33,3.82-3.82,7.26-3.82,5.56,0,8.37,3.6,8.37,9.43Z' fill='%23242265'/%3E%3Cpath d='M380.23,59.38l2.28-4.08c2.01,1.27,4.24,1.96,6.47,1.96s3.5-.95,3.5-2.44c0-1.75-2.23-2.6-4.56-3.5-3.76-1.43-6.68-3.39-6.68-7.26,0-4.35,3.87-6.62,8.37-6.62,2.7,0,5.19,.64,7.74,2.12l-2.01,3.87c-1.75-.9-3.66-1.38-5.25-1.38-1.8,0-3.34,.53-3.34,2.01s1.75,2.44,4.29,3.34c4.13,1.54,7.1,3.5,7.1,7.42,0,4.4-3.55,7.15-8.74,7.15-3.5,0-6.41-.85-9.17-2.6Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M109,88.72h-3.12v-1.82h3.12v-4.27c0-2.93,1.53-5.38,4.85-5.38,1.59,0,2.71,.47,3.87,1.31l-.95,1.48c-.85-.57-1.59-.88-2.68-.88-1.83,0-3.02,1.18-3.02,3.47v4.27h4.92v1.82h-4.92v13.05h-2.07v-13.05Z' fill='%23242265'/%3E%3Cpath d='M117.3,94.34c0-4.58,3.22-7.81,7.73-7.81s7.8,3.23,7.8,7.81-3.22,7.81-7.8,7.81-7.73-3.23-7.73-7.81Zm13.43,0c0-3.43-2.31-5.89-5.7-5.89s-5.63,2.46-5.63,5.89,2.31,5.89,5.63,5.89,5.7-2.42,5.7-5.89Z' fill='%23242265'/%3E%3Cpath d='M145.81,87.11l-.61,1.82c-.58-.2-1.15-.37-2-.37-2.44,0-4.1,1.72-4.1,4.61v8.61h-2.07v-14.87h1.56l.41,2.19c.85-1.55,2.27-2.49,4.37-2.49,.95,0,1.76,.2,2.44,.5Z' fill='%23242265'/%3E%3Cpath d='M154.08,100.09l1.12-1.78c1.56,1.25,3.25,1.82,5.19,1.82,3.15,0,4.92-1.92,4.92-5.48v-15.75h2.2v15.78c0,4.85-2.51,7.5-7.12,7.5-2.34,0-4.37-.67-6.31-2.09Z' fill='%23242265'/%3E%3Cpath d='M185.31,86.9v14.87h-1.59l-.41-2.59c-.88,1.58-2.58,2.86-5.05,2.86-3.73,0-5.46-2.46-5.46-6.09v-9.05h2.07v9.08c0,2.42,.95,4.14,3.63,4.14,2.98,0,4.75-2.66,4.75-5.82v-7.4h2.07Z' fill='%23242265'/%3E%3Cpath d='M205.85,94.27c0,4.58-3.12,7.84-7.43,7.84-2.48,0-4.58-1.11-5.83-2.79,.03,1.14,.07,2.52,.07,4v5.85h-2.07v-22.27h1.56l.44,2.49c1.29-1.72,3.32-2.79,5.87-2.79,4.27,0,7.39,3.23,7.39,7.67Zm-2.07,.1c0-3.43-2.27-5.85-5.49-5.85s-5.73,2.36-5.73,5.75,2.41,5.92,5.73,5.92,5.49-2.42,5.49-5.82Z' fill='%23242265'/%3E%3Cpath d='M221.99,86.9v.07l-9.22,22.21h-2.17v-.07l3.32-7.71-6.54-14.43v-.07h2.17l4.31,9.52c.37,.88,.75,1.72,1.09,2.76,.34-1.04,.68-1.92,1.02-2.76l3.9-9.52h2.14Z' fill='%23242265'/%3E%3Cpath d='M226.36,97.57v-8.85l-2.92-.13v-1.68h2.92v-4.95h2.07v4.95h5.36v1.82h-5.36v8.85c0,1.88,.78,2.52,2.1,2.52,1.05,0,2-.34,2.95-1.01l.92,1.55c-1.12,.84-2.51,1.41-4.07,1.41-2.44,0-3.97-1.41-3.97-4.48Z' fill='%23242265'/%3E%3Cpath d='M250.3,93.73c0,.47-.03,.94-.1,1.45h-12c.34,3.16,2.78,5.05,5.59,5.05,2.1,0,3.42-.64,4.58-1.82l1.19,1.48c-1.53,1.45-3.36,2.25-5.73,2.25-4.54,0-7.73-3.23-7.73-7.84,0-4.31,3.12-7.77,7.56-7.77,4.17,0,6.65,2.86,6.65,7.2Zm-12.04-.37h10c-.07-3.16-1.9-4.91-4.64-4.91s-4.95,1.95-5.36,4.91Z' fill='%23242265'/%3E%3Cpath d='M263.08,87.11l-.61,1.82c-.58-.2-1.15-.37-2-.37-2.44,0-4.1,1.72-4.1,4.61v8.61h-2.07v-14.87h1.56l.41,2.19c.85-1.55,2.27-2.49,4.37-2.49,.95,0,1.76,.2,2.44,.5Z' fill='%23242265'/%3E%3C/g%3E%3C/g%3E%3C/g%3E%3C/svg%3E"
    const jupyterGraphsLogoWhite =
      "data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg id='a' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 398.14 109.18'%3E%3Cg id='b'%3E%3Cpath d='M0,37.41l.09,19.36c.04,9.83,5.33,18.89,13.87,23.77l16.81,9.6c8.54,4.88,19.03,4.83,27.52-.13l16.72-9.76c8.49-4.96,13.69-14.06,13.65-23.9l-.09-19.36c-.05-9.83-5.33-18.89-13.87-23.77L57.89,3.62c-8.54-4.88-19.03-4.83-27.52,.13L13.65,13.51C5.16,18.46-.05,27.57,0,37.41' fill='%23ffffff'/%3E%3Cg id='c'%3E%3Cg%3E%3Cpath d='M42.96,64.19c-.36,1.68-1.19,3.18-2.05,4.66-1.58,2.73-3.04,6.12-.89,9.02,1.71,2.31,5.08,2.85,7.48,1.19,2.92-2.03,2.76-5.81,1.24-8.65-.78-1.45-1.7-2.81-2.33-4.34-.69-1.67-.93-3.42-.97-5.22,0-.36,0-.73-.01-1.09h-2.11c0,1.48-.05,2.99-.36,4.43Z' fill='%23242265'/%3E%3Cpath d='M42.96,29.53c-.36-1.68-1.19-3.18-2.05-4.66-1.58-2.73-3.04-6.12-.89-9.02,1.71-2.31,5.08-2.85,7.48-1.19,2.92,2.03,2.76,5.81,1.24,8.65-.78,1.45-1.7,2.81-2.33,4.34-.69,1.67-.93,3.42-.97,5.22,0,.36,0,.73-.01,1.09h-2.11c0-1.48-.05-2.99-.36-4.43Z' fill='%23242265'/%3E%3Crect x='43.32' y='33.66' width='2.11' height='26.44' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M30.07,56.75c-1.27,1.15-2.16,2.63-3.01,4.1-1.57,2.73-3.78,5.69-7.37,5.28-2.86-.32-5.01-2.97-4.77-5.88,.3-3.55,3.65-5.3,6.87-5.4,1.64-.05,3.28,.06,4.92-.15,1.8-.24,3.43-.9,5.01-1.77,.32-.18,.63-.35,.95-.53l1.05,1.83c-1.29,.73-2.56,1.54-3.65,2.53Z' fill='%23242265'/%3E%3Cpath d='M60.09,39.42c1.63-.53,3.35-.56,5.06-.55,3.15,0,6.82-.43,8.26-3.74,1.15-2.64-.07-5.83-2.71-7.07-3.22-1.52-6.41,.51-8.11,3.25-.87,1.4-1.58,2.87-2.59,4.19-1.1,1.44-2.5,2.52-4.04,3.45-.31,.19-.62,.37-.94,.55l1.05,1.83c1.28-.75,2.62-1.45,4.01-1.9Z' fill='%23242265'/%3E%3Crect x='43.3' y='33.65' width='2.11' height='26.44' transform='translate(25.94 108.72) rotate(-120)' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M60.09,54.3c1.63,.53,3.35,.56,5.06,.55,3.15,0,6.82,.43,8.26,3.74,1.15,2.64-.07,5.83-2.71,7.07-3.22,1.52-6.41-.51-8.11-3.25-.87-1.4-1.58-2.87-2.59-4.19-1.1-1.44-2.5-2.52-4.04-3.45-.31-.19-.62-.37-.94-.55l1.05-1.83c1.28,.75,2.62,1.45,4.01,1.9Z' fill='%23242265'/%3E%3Cpath d='M30.07,36.97c-1.27-1.15-2.16-2.63-3.01-4.1-1.57-2.73-3.78-5.69-7.37-5.28-2.86,.32-5.01,2.97-4.77,5.88,.3,3.55,3.65,5.3,6.87,5.4,1.64,.05,3.28-.06,4.92,.15,1.8,.24,3.43,.9,5.01,1.77,.32,.18,.63,.35,.95,.53l1.05-1.83c-1.29-.73-2.56-1.54-3.65-2.53Z' fill='%23242265'/%3E%3Crect x='43.34' y='33.65' width='2.11' height='26.44' transform='translate(107.18 31.86) rotate(120)' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M66.99,50.35c-.36,1.68-1.19,3.18-2.05,4.66-1.58,2.73-3.04,6.12-.89,9.02,1.71,2.31,5.08,2.85,7.48,1.19,2.92-2.03,2.76-5.81,1.24-8.65-.78-1.45-1.7-2.81-2.33-4.34-.69-1.67-.93-3.42-.97-5.22,0-.36,0-.73-.01-1.09h-2.11c0,1.48-.05,2.99-.36,4.43Z' fill='%23242265'/%3E%3Cpath d='M66.99,43.37c-.36-1.68-1.19-3.18-2.05-4.66-1.58-2.73-3.04-6.12-.89-9.02,1.71-2.31,5.08-2.85,7.48-1.19,2.92,2.03,2.76,5.81,1.24,8.65-.78,1.45-1.7,2.81-2.33,4.34-.69,1.67-.93,3.42-.97,5.22,0,.36,0,.73-.01,1.09h-2.11c0-1.48-.05-2.99-.36-4.43Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M18.87,50.35c-.36,1.68-1.19,3.18-2.05,4.66-1.58,2.73-3.04,6.12-.89,9.02,1.71,2.31,5.08,2.85,7.48,1.19,2.92-2.03,2.76-5.81,1.24-8.65-.78-1.45-1.7-2.81-2.33-4.34-.69-1.67-.93-3.42-.97-5.22,0-.36,0-.73-.01-1.09h-2.11c0,1.48-.05,2.99-.36,4.43Z' fill='%23242265'/%3E%3Cpath d='M18.87,43.37c-.36-1.68-1.19-3.18-2.05-4.66-1.58-2.73-3.04-6.12-.89-9.02,1.71-2.31,5.08-2.85,7.48-1.19,2.92,2.03,2.76,5.81,1.24,8.65-.78,1.45-1.7,2.81-2.33,4.34-.69,1.67-.93,3.42-.97,5.22,0,.36,0,.73-.01,1.09h-2.11c0-1.48-.05-2.99-.36-4.43Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M30.02,29.06c-1.27,1.15-2.16,2.63-3.01,4.1-1.57,2.73-3.78,5.69-7.37,5.28-2.86-.32-5.01-2.97-4.77-5.88,.3-3.55,3.65-5.3,6.87-5.4,1.64-.05,3.28,.06,4.92-.15,1.8-.24,3.43-.9,5.01-1.77,.32-.18,.63-.35,.95-.53l1.05,1.83c-1.29,.73-2.56,1.54-3.65,2.53Z' fill='%23242265'/%3E%3Cpath d='M36.06,25.58c1.63-.53,3.35-.56,5.06-.55,3.15,0,6.82-.43,8.26-3.74,1.15-2.64-.07-5.83-2.71-7.07-3.22-1.52-6.41,.51-8.11,3.25-.87,1.4-1.58,2.87-2.59,4.19-1.1,1.44-2.5,2.52-4.04,3.45-.31,.19-.62,.37-.94,.55l1.05,1.83c1.28-.75,2.62-1.45,4.01-1.9Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M54.1,70.6c-1.27,1.15-2.16,2.63-3.01,4.1-1.57,2.73-3.78,5.69-7.37,5.28-2.86-.32-5.01-2.97-4.77-5.88,.3-3.55,3.65-5.3,6.87-5.4,1.64-.05,3.28,.06,4.92-.15,1.8-.24,3.43-.9,5.01-1.77,.32-.18,.63-.35,.95-.53l1.05,1.83c-1.29,.73-2.56,1.54-3.65,2.53Z' fill='%23242265'/%3E%3Cpath d='M60.14,67.12c1.63-.53,3.35-.56,5.06-.55,3.15,0,6.82-.43,8.26-3.74,1.15-2.64-.07-5.83-2.71-7.07-3.22-1.52-6.41,.51-8.11,3.25-.87,1.4-1.58,2.87-2.59,4.19-1.1,1.44-2.5,2.52-4.04,3.45-.31,.19-.62,.37-.94,.55l1.05,1.83c1.28-.75,2.62-1.45,4.01-1.9Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M58.73,29.06c1.27,1.15,2.16,2.63,3.01,4.1,1.57,2.73,3.78,5.69,7.37,5.28,2.86-.32,5.01-2.97,4.77-5.88-.3-3.55-3.65-5.3-6.87-5.4-1.64-.05-3.28,.06-4.92-.15-1.8-.24-3.43-.9-5.01-1.77-.32-.18-.63-.35-.95-.53l-1.05,1.83c1.29,.73,2.56,1.54,3.65,2.53Z' fill='%23242265'/%3E%3Cpath d='M52.69,25.58c-1.63-.53-3.35-.56-5.06-.55-3.15,0-6.82-.43-8.26-3.74-1.15-2.64,.07-5.83,2.71-7.07,3.22-1.52,6.41,.51,8.11,3.25,.87,1.4,1.58,2.87,2.59,4.19,1.1,1.44,2.5,2.52,4.04,3.45,.31,.19,.62,.37,.94,.55l-1.05,1.83c-1.28-.75-2.62-1.45-4.01-1.9Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M34.64,70.6c1.27,1.15,2.16,2.63,3.01,4.1,1.57,2.73,3.78,5.69,7.37,5.28,2.86-.32,5.01-2.97,4.77-5.88-.3-3.55-3.65-5.3-6.87-5.4-1.64-.05-3.28,.06-4.92-.15-1.8-.24-3.43-.9-5.01-1.77-.32-.18-.63-.35-.95-.53l-1.05,1.83c1.29,.73,2.56,1.54,3.65,2.53Z' fill='%23242265'/%3E%3Cpath d='M28.6,67.12c-1.63-.53-3.35-.56-5.06-.55-3.15,0-6.82-.43-8.26-3.74-1.15-2.64,.07-5.83,2.71-7.07,3.22-1.52,6.41,.51,8.11,3.25,.87,1.4,1.58,2.87,2.59,4.19,1.1,1.44,2.5,2.52,4.04,3.45,.31,.19,.62,.37,.94,.55l-1.05,1.83c-1.28-.75-2.62-1.45-4.01-1.9Z' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cg%3E%3Cpath d='M61.95,41.28c.53-1.63,.56-3.35,.55-5.06,0-3.15,.43-6.82,3.74-8.26,2.64-1.15,5.83,.07,7.07,2.71,1.52,3.22-.51,6.41-3.25,8.11-1.4,.87-2.87,1.58-4.19,2.59-1.44,1.1-2.52,2.5-3.45,4.04-.19,.31-.37,.62-.55,.94l-1.83-1.05c.75-1.28,1.45-2.62,1.9-4.01Z' fill='%23242265'/%3E%3Cpath d='M48.36,64.86c-1.15,1.27-2.63,2.16-4.1,3.01-2.73,1.57-5.69,3.78-5.28,7.37,.32,2.86,2.97,5.01,5.88,4.77,3.55-.3,5.3-3.65,5.4-6.87,.05-1.64-.06-3.28,.15-4.92,.24-1.8,.9-3.43,1.77-5.01,.18-.32,.35-.63,.53-.95l-1.83-1.05c-.73,1.29-1.54,2.56-2.53,3.65Z' fill='%23242265'/%3E%3Crect x='55.82' y='42.51' width='2.11' height='20.88' transform='translate(34.09 -21.34) rotate(30)' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M26.79,41.28c-.53-1.63-.56-3.35-.55-5.06,0-3.15-.43-6.82-3.74-8.26-2.64-1.15-5.83,.07-7.07,2.71-1.52,3.22,.51,6.41,3.25,8.11,1.4,.87,2.87,1.58,4.19,2.59,1.44,1.1,2.52,2.5,3.45,4.04,.19,.31,.37,.62,.55,.94l1.83-1.05c-.75-1.28-1.45-2.62-1.9-4.01Z' fill='%23242265'/%3E%3Cpath d='M40.39,64.86c1.15,1.27,2.63,2.16,4.1,3.01,2.73,1.57,5.69,3.78,5.28,7.37-.32,2.86-2.97,5.01-5.88,4.77-3.55-.3-5.3-3.65-5.4-6.87-.05-1.64,.06-3.28-.15-4.92-.24-1.8-.9-3.43-1.77-5.01-.18-.32-.35-.63-.53-.95l1.83-1.05c.73,1.29,1.54,2.56,2.53,3.65Z' fill='%23242265'/%3E%3Crect x='30.82' y='42.51' width='2.11' height='20.88' transform='translate(85.95 82.86) rotate(150)' fill='%23242265'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M57.96,34.4c1.68,.36,3.18,1.19,4.66,2.05,2.73,1.58,6.12,3.04,9.02,.89,2.31-1.71,2.85-5.08,1.19-7.48-2.03-2.92-5.81-2.76-8.65-1.24-1.45,.78-2.81,1.7-4.34,2.33-1.67,.69-3.42,.93-5.22,.97-.36,0-.73,0-1.09,.01v2.11c1.48,0,2.99,.05,4.43,.36Z' fill='%23242265'/%3E%3Cpath d='M30.75,34.39c-1.68,.36-3.18,1.19-4.66,2.05-2.73,1.58-6.12,3.04-9.02,.89-2.31-1.71-2.85-5.08-1.19-7.48,2.03-2.92,5.81-2.76,8.65-1.24,1.45,.78,2.81,1.7,4.34,2.33,1.67,.69,3.42,.93,5.22,.97,.36,0,.73,0,1.09,.01v2.11c-1.48,0-2.99,.05-4.43,.36Z' fill='%23242265'/%3E%3Crect x='44.26' y='22.53' width='2.11' height='20.88' transform='translate(12.35 78.29) rotate(-90)' fill='%23242265'/%3E%3C/g%3E%3C/g%3E%3Ccircle cx='44.37' cy='19.13' r='5.43' fill='%23242265'/%3E%3Ccircle cx='44.37' cy='74.59' r='5.43' fill='%23242265'/%3E%3Ccircle cx='68.39' cy='32.99' r='5.43' fill='%23242265'/%3E%3Ccircle cx='20.36' cy='60.72' r='5.43' fill='%23242265'/%3E%3Ccircle cx='20.36' cy='32.99' r='5.43' fill='%23242265'/%3E%3Ccircle cx='68.39' cy='60.72' r='5.43' fill='%23242265'/%3E%3C/g%3E%3Cg id='d'%3E%3Cg%3E%3Cpath d='M130.81,37.81v.16l-13.94,35.13h-6.15v-.11l5.25-12.14-10.12-22.89v-.16h6.25l5.03,12.08c.58,1.43,1.11,2.86,1.59,4.61,.48-1.75,.95-3.18,1.43-4.61l4.61-12.08h6.04Z' fill='%23ffffff'/%3E%3Cpath d='M135.69,25.41h22.52v5.78h-16.27v10.39h14.57v5.62h-14.57v14.25h-6.25V25.41Z' fill='%23ffffff'/%3E%3Cpath d='M162.72,29.44c0-1.91,1.38-3.44,3.6-3.44s3.6,1.54,3.6,3.5-1.43,3.39-3.6,3.39-3.6-1.54-3.6-3.44Zm.69,8.37h5.78v23.63h-5.78v-23.63Z' fill='%23ffffff'/%3E%3Cpath d='M175.97,23.29h5.78l.05,38.15h-5.83V23.29Z' fill='%23ffffff'/%3E%3Cpath d='M210.04,48.78c0,.85-.11,1.8-.21,2.76h-16.96c.74,3.82,3.71,5.83,7.53,5.83,2.7,0,4.61-.79,6.25-2.23l2.44,3.71c-2.7,2.17-5.56,3.29-9.22,3.29-7.58,0-12.77-5.14-12.77-12.56,0-6.94,5.03-12.4,12.19-12.4,6.68,0,10.76,4.5,10.76,11.61Zm-17.12-1.17h11.66c-.16-3.76-2.38-5.72-5.41-5.72s-5.62,2.07-6.25,5.72Z' fill='%23ffffff'/%3E%3Cpath d='M213.39,59.38l2.28-4.08c2.01,1.27,4.24,1.96,6.47,1.96s3.5-.95,3.5-2.44c0-1.75-2.23-2.6-4.56-3.5-3.76-1.43-6.68-3.39-6.68-7.26,0-4.35,3.87-6.62,8.37-6.62,2.7,0,5.19,.64,7.74,2.12l-2.01,3.87c-1.75-.9-3.66-1.38-5.25-1.38-1.8,0-3.34,.53-3.34,2.01s1.75,2.44,4.29,3.34c4.13,1.54,7.1,3.5,7.1,7.42,0,4.4-3.55,7.15-8.74,7.15-3.5,0-6.41-.85-9.17-2.6Z' fill='%23ffffff'/%3E%3Cpath d='M271.74,37.81v24.59c0,7.58-5.14,11.34-12.4,11.34-4.34,0-7.79-1.22-10.7-3.6l2.23-4.35c2.17,1.75,4.77,2.76,8,2.76,4.29,0,7.05-2.01,7.05-6.04,0-1.22,.05-2.54,.11-3.87-2.07,2.17-4.88,3.23-7.84,3.23-6.73,0-11.34-5.09-11.34-12.29s4.61-12.35,11.23-12.35c3.55,0,6.68,1.32,8.69,4.03l1.17-3.44h3.82Zm-5.56,11.76c0-4.19-2.38-7.31-6.78-7.31s-6.68,3.02-6.68,7.31,2.54,7.31,6.62,7.31c4.45,0,6.84-3.13,6.84-7.31Z' fill='%23ffffff'/%3E%3Cpath d='M294.47,38.29l-1.48,4.88c-.9-.32-1.85-.53-3.07-.53-3.34,0-5.62,2.17-5.62,5.94v12.88h-5.78v-23.63h3.92l1.11,3.5c1.38-2.65,3.76-4.03,6.84-4.03,1.64,0,2.97,.37,4.08,1.01Z' fill='%23ffffff'/%3E%3Cpath d='M317.37,46.18v15.26h-3.87l-1.06-3.55c-1.75,2.49-4.56,4.03-8.43,4.03-4.34,0-7.42-2.44-7.42-6.62,0-5.4,4.77-8.37,11.98-8.37,1.22,0,2.12,.05,2.97,.11v-1.06c0-2.44-1.8-3.66-4.82-3.66-2.33,0-4.93,.74-7.37,1.91l-1.64-4.4c3.5-1.59,6.73-2.44,9.91-2.44,6.04,0,9.75,3.07,9.75,8.8Zm-5.67,4.61c-.95-.11-1.7-.16-2.76-.16-4.19,0-6.62,1.48-6.62,4.08,0,1.85,1.27,2.86,3.39,2.86,3.39,0,5.88-2.49,5.99-6.78Z' fill='%23ffffff'/%3E%3Cpath d='M348.74,49.52c0,7.37-4.72,12.51-11.29,12.51-3.29,0-6.04-1.27-7.95-3.29,.11,1.64,.11,3.55,.11,5.62v8.74h-5.78V37.81h3.92l1.11,3.6c1.96-2.6,4.93-4.19,8.58-4.19,6.52,0,11.29,5.19,11.29,12.29Zm-5.88,.16c0-4.4-2.65-7.37-6.62-7.37s-6.84,2.91-6.84,7.26,2.81,7.42,6.84,7.42,6.62-3.02,6.62-7.31Z' fill='%23ffffff'/%3E%3Cpath d='M375.51,46.61v14.84h-5.78v-14.36c0-2.86-1.22-4.72-4.08-4.72-3.76,0-5.72,3.13-5.72,6.89v12.19h-5.78V23.29h5.78v14.1c0,1.11,0,2.17-.05,3.6,1.48-2.33,3.82-3.82,7.26-3.82,5.56,0,8.37,3.6,8.37,9.43Z' fill='%23ffffff'/%3E%3Cpath d='M380.23,59.38l2.28-4.08c2.01,1.27,4.24,1.96,6.47,1.96s3.5-.95,3.5-2.44c0-1.75-2.23-2.6-4.56-3.5-3.76-1.43-6.68-3.39-6.68-7.26,0-4.35,3.87-6.62,8.37-6.62,2.7,0,5.19,.64,7.74,2.12l-2.01,3.87c-1.75-.9-3.66-1.38-5.25-1.38-1.8,0-3.34,.53-3.34,2.01s1.75,2.44,4.29,3.34c4.13,1.54,7.1,3.5,7.1,7.42,0,4.4-3.55,7.15-8.74,7.15-3.5,0-6.41-.85-9.17-2.6Z' fill='%23ffffff'/%3E%3C/g%3E%3Cg%3E%3Cpath d='M109,88.72h-3.12v-1.82h3.12v-4.27c0-2.93,1.53-5.38,4.85-5.38,1.59,0,2.71,.47,3.87,1.31l-.95,1.48c-.85-.57-1.59-.88-2.68-.88-1.83,0-3.02,1.18-3.02,3.47v4.27h4.92v1.82h-4.92v13.05h-2.07v-13.05Z' fill='%23ffffff'/%3E%3Cpath d='M117.3,94.34c0-4.58,3.22-7.81,7.73-7.81s7.8,3.23,7.8,7.81-3.22,7.81-7.8,7.81-7.73-3.23-7.73-7.81Zm13.43,0c0-3.43-2.31-5.89-5.7-5.89s-5.63,2.46-5.63,5.89,2.31,5.89,5.63,5.89,5.7-2.42,5.7-5.89Z' fill='%23ffffff'/%3E%3Cpath d='M145.81,87.11l-.61,1.82c-.58-.2-1.15-.37-2-.37-2.44,0-4.1,1.72-4.1,4.61v8.61h-2.07v-14.87h1.56l.41,2.19c.85-1.55,2.27-2.49,4.37-2.49,.95,0,1.76,.2,2.44,.5Z' fill='%23ffffff'/%3E%3Cpath d='M154.08,100.09l1.12-1.78c1.56,1.25,3.25,1.82,5.19,1.82,3.15,0,4.92-1.92,4.92-5.48v-15.75h2.2v15.78c0,4.85-2.51,7.5-7.12,7.5-2.34,0-4.37-.67-6.31-2.09Z' fill='%23ffffff'/%3E%3Cpath d='M185.31,86.9v14.87h-1.59l-.41-2.59c-.88,1.58-2.58,2.86-5.05,2.86-3.73,0-5.46-2.46-5.46-6.09v-9.05h2.07v9.08c0,2.42,.95,4.14,3.63,4.14,2.98,0,4.75-2.66,4.75-5.82v-7.4h2.07Z' fill='%23ffffff'/%3E%3Cpath d='M205.85,94.27c0,4.58-3.12,7.84-7.43,7.84-2.48,0-4.58-1.11-5.83-2.79,.03,1.14,.07,2.52,.07,4v5.85h-2.07v-22.27h1.56l.44,2.49c1.29-1.72,3.32-2.79,5.87-2.79,4.27,0,7.39,3.23,7.39,7.67Zm-2.07,.1c0-3.43-2.27-5.85-5.49-5.85s-5.73,2.36-5.73,5.75,2.41,5.92,5.73,5.92,5.49-2.42,5.49-5.82Z' fill='%23ffffff'/%3E%3Cpath d='M221.99,86.9v.07l-9.22,22.21h-2.17v-.07l3.32-7.71-6.54-14.43v-.07h2.17l4.31,9.52c.37,.88,.75,1.72,1.09,2.76,.34-1.04,.68-1.92,1.02-2.76l3.9-9.52h2.14Z' fill='%23ffffff'/%3E%3Cpath d='M226.36,97.57v-8.85l-2.92-.13v-1.68h2.92v-4.95h2.07v4.95h5.36v1.82h-5.36v8.85c0,1.88,.78,2.52,2.1,2.52,1.05,0,2-.34,2.95-1.01l.92,1.55c-1.12,.84-2.51,1.41-4.07,1.41-2.44,0-3.97-1.41-3.97-4.48Z' fill='%23ffffff'/%3E%3Cpath d='M250.3,93.73c0,.47-.03,.94-.1,1.45h-12c.34,3.16,2.78,5.05,5.59,5.05,2.1,0,3.42-.64,4.58-1.82l1.19,1.48c-1.53,1.45-3.36,2.25-5.73,2.25-4.54,0-7.73-3.23-7.73-7.84,0-4.31,3.12-7.77,7.56-7.77,4.17,0,6.65,2.86,6.65,7.2Zm-12.04-.37h10c-.07-3.16-1.9-4.91-4.64-4.91s-4.95,1.95-5.36,4.91Z' fill='%23ffffff'/%3E%3Cpath d='M263.08,87.11l-.61,1.82c-.58-.2-1.15-.37-2-.37-2.44,0-4.1,1.72-4.1,4.61v8.61h-2.07v-14.87h1.56l.41,2.19c.85-1.55,2.27-2.49,4.37-2.49,.95,0,1.76,.2,2.44,.5Z' fill='%23ffffff'/%3E%3C/g%3E%3C/g%3E%3C/g%3E%3C/svg%3E"
    logo.src = isDarkTheme ? jupyterGraphsLogoWhite : jupyterGraphsLogoBlue
    logo.height = 80
    logo.className = 'yfiles-graphs-for-jupyter-logo'
    const yFilesJupyterLink = document.createElement('a') as HTMLAnchorElement
    yFilesJupyterLink.href = appendCampaign(
      'https://www.yworks.com/products/yfiles-graphs-for-jupyter',
      'about'
    )
    yFilesJupyterLink.target = '_blank'
    yFilesJupyterLink.appendChild(logo)
    about.appendChild(yFilesJupyterLink)

    const p1 = document.createElement('p')
    p1.innerHTML =
      'This graph visualization widget is powered by ' +
      `<a href="${appendCampaign(
        'https://yworks.com/products/yfiles',
        'about'
      )}" target="_blank">yFiles</a> &#8212; the superior diagramming SDK<br>for ` +
      `<a href="${appendCampaign(
        'https://yworks.com/products/yfiles/platforms#web-platform',
        'about'
      )}" target="_blank">web</a>, ` +
      `<a href="${appendCampaign(
        'https://yworks.com/products/yfiles/platforms#java-platform',
        'about'
      )}" target="_blank">Java</a>, and ` +
      `<a href="${appendCampaign(
        'https://yworks.com/products/yfiles/platforms#dotnet-platform',
        'about'
      )}">.NET</a>.`
    about.appendChild(p1)

    const p2 = document.createElement('p')
    p2.innerHTML =
      'For documentation, feedback or bug reports visit: ' +
      '<a href="https://github.com/yWorks/yfiles-jupyter-graphs" target="_blank">github.com/yWorks/yfiles-jupyter-graphs</a>'
    const downloadInfoContainer = document.createElement('div')
    downloadInfoContainer.className = 'icon-container'
    downloadInfoContainer.appendChild(createMdiIconSpan(this.el, mdiDownload))
    downloadInfoContainer.appendChild(p2)
    about.appendChild(downloadInfoContainer)

    const cta = document.createElement('p')
    cta.className = 'cta'
    cta.innerHTML =
      `If you are interested in the <a href="${appendCampaign(
        'https://my.yworks.com/signup',
        'about'
      )}" target="_blank">yFiles for HTML</a> library, ` +
      `start your free evaluation <a href="${appendCampaign(
        'https://my.yworks.com/signup',
        'about'
      )}" target="_blank">here</a>!`
    const ctaContainer = document.createElement('div')
    ctaContainer.className = 'icon-container'
    ctaContainer.appendChild(createMdiIconSpan(this.el, mdiGithub))
    ctaContainer.appendChild(cta)
    about.appendChild(ctaContainer)

    const aboutFooter = document.createElement('div')
    aboutFooter.className = 'about-footer'

    const yWorksFooterLogo = new Image()
    const yWorksBlue =
      "data:image/svg+xml,%3C%3Fxml version='1.0' encoding='utf-8'%3F%3E%3Csvg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 1000 394.6' style='enable-background:new 0 0 1000 394.6;' xml:space='preserve'%3E%3Cstyle type='text/css'%3E .st0%7Bfill:%23242265;%7D .st1%7Bfill:%23FF6C00;%7D%0A%3C/style%3E%3Cg id='yWorks_1_'%3E%3Cpath class='st0' d='M645.7,197c0-28.6,20.6-48.8,49.6-48.8s49.8,20.1,49.8,48.8s-20.7,48.9-49.8,48.9 C666.2,245.9,645.7,225.6,645.7,197 M722.1,197c0-17-10.8-28.8-26.7-28.8c-15.8,0-26.7,11.8-26.7,28.8s11,28.9,26.7,28.9 C711.3,225.8,722.1,213.9,722.1,197'/%3E%3Cpath class='st0' d='M822.2,152.6l-5.8,19.1c-3.5-1.3-7.3-2.1-12-2.1c-13,0-22,8.5-22,23.2v50.4h-22.6v-92.6h15.3l4.4,13.7 c5.4-10.4,14.7-15.8,26.7-15.8C812.7,148.6,817.9,150.1,822.2,152.6'/%3E%3Cpath class='st1' d='M534.5,150.7v0.6l-48.6,122.8h-24v-0.4l14.6-32.7l-39.7-89.7v-0.6h24.5l25.8,62l23.7-62.1L534.5,150.7 L534.5,150.7z'/%3E%3Cpath class='st0' d='M621.8,150.7l-14.3,41.1c-1.3,3.5-2.5,7.3-3.5,11.4c-1.6-4.1-3.3-7.9-5.4-11.7l-18.1-36.3h-4.8l-18,36.4 c-1.9,3.8-3.5,7.3-5.1,11.4c-1-3.9-2.1-7.5-3.3-11.2L538.5,161l-12.3,31.3l19.4,51.8h6.9l26-51.7l25.7,51.7h7l34.6-92.7v-0.6H621.8 z'/%3E%3Cpath class='st0' d='M947.6,188.2c-9.9-3.5-16.8-7-16.8-13.1c0-5.8,6-7.9,13.1-7.9c6.3,0,13.7,1.9,20.6,5.4l7.9-15.2 c-9.9-5.8-19.7-8.3-30.3-8.3c-17.7,0-32.7,8.9-32.7,26c0,15.2,11.4,22.8,26.1,28.5c9.1,3.5,17.8,6.9,17.8,13.7 c0,5.8-5.4,9.5-13.7,9.5c-8.7,0-17.4-2.7-25.3-7.7l-1.5-1v21.1c8.7,4.1,17.8,6.2,28.5,6.2c20.3,0,34.2-10.8,34.2-28 C975.4,201.9,963.8,194.2,947.6,188.2'/%3E%3Cpolygon class='st0' points='902.2,230.6 872,195.5 902.2,159.5 902.2,150.7 883.2,150.7 852.5,187.4 852.5,118.7 829.8,118.7 829.8,243.2 852.5,243.2 852.5,203.7 885.7,243.2 902.2,243.2 '/%3E%3C/g%3E%3Cpath class='st0' d='M25.5,160.3l0.4,75.4c0.2,38.3,20.8,73.6,54,92.6l65.5,37.4c33.3,19,74.1,18.8,107.2-0.5l65.1-38 c33.1-19.3,53.4-54.8,53.2-93.1l-0.4-75.4c-0.2-38.3-20.8-73.6-54-92.6L251,28.7c-33.3-19-74.1-18.8-107.2,0.5l-65.2,38 C45.6,86.5,25.4,122,25.5,160.3'/%3E%3Cpath class='st1' d='M127.2,172.3c-5.2,0-9.9,0.3-14.5-1c-9.1-2.4-15.3-7.9-17.5-17.3c-2.6-10.6,4.3-21.9,14.8-24.8 c7.8-2.1,14.7-0.1,20.9,4.8c4.3,3.4,7,7.9,9.6,12.5c2.4,4.3,4.8,8.7,7.8,12.6c3.7,4.8,8.2,8.7,13.4,11.9c5.2,3.3,10.4,6.4,15.9,9.1 c7.9,3.9,16.2,6,25.3,5c8.4-0.9,15.8-4.3,22.9-8.5c3.1-1.9,6.3-3.6,9.5-5.6c7.3-4.5,13-10.6,17.3-17.9c2.7-4.6,5.1-9.4,8.3-13.8 c3.8-5.3,8.7-9,15.1-10.5c9.5-2.2,20.6,2.7,24.6,12.7c4.5,11.4-1.2,23.8-12.8,28.4c-3.9,1.6-7.9,2.3-12.1,2.3c-3.7,0-7.3,0-11,0 c-6.1,0-12.2,0.9-18,2.9c-4.1,1.4-7.9,3.6-11.7,5.7c-3.7,2.1-7.4,4.2-10.9,6.5c-6.3,4-11.5,9-15.2,15.5c-3.2,5.6-5.2,11.6-5.8,18.1 c-0.5,5.5-0.4,11-0.4,16.6c0,5.9,0.4,11.7,2.2,17.3c1.3,4.3,3.3,8.4,5.5,12.3c2.9,5.3,6.4,10.3,8.3,16.1c1.9,6.1,1.9,12.1-0.8,17.9 c-3.4,7-8.9,11.2-16.7,12.1c-7,0.9-13-1.4-17.8-6.3c-5-5.1-6.9-11.6-5.9-18.8c0.9-6.8,4.3-12.5,7.7-18.2c3.6-5.9,6.8-11.9,8.1-18.8 c0.5-2.4,0.7-4.8,0.9-7.3c0.4-5.3,0.4-10.5,0.3-15.8c-0.2-6.8-0.6-13.6-3.5-19.9c-2.2-4.9-4.9-9.5-8.7-13.4 c-4.1-4.2-8.9-7.5-13.9-10.5c-4.1-2.4-8.2-4.9-12.5-7c-5.9-2.9-12.1-4.5-18.6-5C133.5,172.3,130.1,172.5,127.2,172.3z'/%3E%3C/svg%3E"
    const yWorksWhite =
      "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 290.55 111.66'%3E%3Cdefs%3E%3Cstyle%3E.cls-1%7Bfill:none;%7D.cls-2%7Bclip-path:url(%23clip-path);%7D.cls-3%7Bfill:%23fff;%7D%3C/style%3E%3CclipPath id='clip-path' transform='translate(0 0)'%3E%3Crect class='cls-1' width='290.55' height='111.66'/%3E%3C/clipPath%3E%3C/defs%3E%3Cg id='yWorks_-_H_-_weiss' data-name='yWorks - H - weiss'%3E%3Cg class='cls-2'%3E%3Cg class='cls-2'%3E%3Cpath class='cls-3' d='M189.73,55.77c0-8.75,6.3-14.93,15.18-14.93S220.14,47,220.14,55.77s-6.33,15-15.23,15-15.18-6.21-15.18-15m23.37,0c0-5.2-3.3-8.81-8.16-8.81s-8.17,3.61-8.17,8.81,3.36,8.84,8.17,8.84,8.16-3.67,8.16-8.84' transform='translate(0 0)'/%3E%3Cpath class='cls-3' d='M243.84,42.09l-1.77,5.84a10.22,10.22,0,0,0-3.68-.64c-4,0-6.73,2.59-6.73,7.08V69.76h-6.92V41.48h4.68l1.35,4.19A8.68,8.68,0,0,1,239,40.84a9.81,9.81,0,0,1,4.89,1.25' transform='translate(0 0)'/%3E%3Cpolygon class='cls-3' points='155.84 41.48 155.84 41.67 140.94 79.39 133.58 79.39 133.58 79.23 137.97 69.23 125.76 41.79 125.76 41.48 133.32 41.48 141.21 60.57 148.46 41.78 155.71 41.48 155.84 41.48'/%3E%3Cpath class='cls-3' d='M182.62,41.61l-4.57,12.57A29.36,29.36,0,0,0,177,57.67a27.76,27.76,0,0,0-1.66-3.58L169.79,43h-1.3L163,54.07c-.58,1.16-1.07,2.23-1.56,3.48-.3-1.19-.64-2.29-1-3.41l-3.29-9.39-3.75,9.54,5.91,15.77h2.1l7.92-15.74,7.83,15.74h2.13l10.54-28.23v0h-7.22Z' transform='translate(0 0)'/%3E%3Cpath class='cls-3' d='M282,53.08c-3-1.07-5.14-2.14-5.14-4s1.83-2.42,4-2.42a14.36,14.36,0,0,1,6.31,1.66l2.41-4.65a17.68,17.68,0,0,0-9.27-2.54c-5.41,0-10,2.72-10,8,0,4.65,3.49,7,8,8.72,2.79,1.07,5.45,2.11,5.45,4.19,0,1.77-1.65,2.91-4.19,2.91a14.51,14.51,0,0,1-7.74-2.36l-.46-.31v6.46a19.89,19.89,0,0,0,8.72,1.9c6.21,0,10.46-3.31,10.46-8.57,0-4.74-3.58-7.1-8.53-8.93' transform='translate(0 0)'/%3E%3Cpolygon class='cls-3' points='268.36 66.17 259.04 55.33 268.36 44.2 268.36 41.48 262.5 41.48 253.02 52.82 253.02 31.86 246.1 31.86 246.1 70.06 253.02 70.06 253.02 57.86 263.27 70.06 268.36 70.06 268.36 66.17'/%3E%3Cpath class='cls-3' d='M0,44.55v0Z' transform='translate(0 0)'/%3E%3Cpath class='cls-3' d='M105.48,44.06A32.82,32.82,0,0,0,89,15.75l-20-11.43a32.76,32.76,0,0,0-32.77.15L16.23,16.09A32.86,32.86,0,0,0,0,44.53L.12,67.6A32.82,32.82,0,0,0,16.63,95.91l20,11.44a32.76,32.76,0,0,0,32.77-.16L89.34,95.58A32.79,32.79,0,0,0,105.6,67.11ZM80.24,47.4a9.55,9.55,0,0,1-3.7.7H73.18a16.91,16.91,0,0,0-5.51.89,23.18,23.18,0,0,0-3.58,1.74c-1.13.65-2.26,1.29-3.33,2a13.53,13.53,0,0,0-4.65,4.74A13.68,13.68,0,0,0,54.33,63c-.15,1.68-.12,3.37-.12,5.08a17.12,17.12,0,0,0,.67,5.29,18.41,18.41,0,0,0,1.69,3.76,31,31,0,0,1,2.53,4.93,7.32,7.32,0,0,1-.24,5.48,6.49,6.49,0,0,1-10.55,1.77,6.59,6.59,0,0,1-1.81-5.75A14.81,14.81,0,0,1,48.86,78a17,17,0,0,0,2.47-5.75A16.37,16.37,0,0,0,51.61,70c.12-1.63.12-3.22.09-4.84a15.27,15.27,0,0,0-1.07-6.09A13.92,13.92,0,0,0,48,55a20.78,20.78,0,0,0-4.25-3.22c-1.26-.73-2.51-1.5-3.83-2.14A15.48,15.48,0,0,0,34.2,48.1c-1.16,0-2.2.09-3.09,0a16.41,16.41,0,0,1-4.43-.3,6.87,6.87,0,0,1-5.36-5.3A6.47,6.47,0,0,1,25.85,35a6.93,6.93,0,0,1,6.39,1.47,12.12,12.12,0,0,1,2.94,3.82,30.94,30.94,0,0,0,2.39,3.85,15.08,15.08,0,0,0,4.1,3.65,54.39,54.39,0,0,0,4.86,2.78,13.83,13.83,0,0,0,7.74,1.53,17.56,17.56,0,0,0,7-2.6c.94-.58,1.92-1.1,2.9-1.71a15.71,15.71,0,0,0,5.3-5.48A46.62,46.62,0,0,1,72,38a7.77,7.77,0,0,1,4.62-3.21A6.55,6.55,0,0,1,80.24,47.4' transform='translate(0 0)'/%3E%3C/g%3E%3C/g%3E%3C/g%3E%3C/svg%3E"
    yWorksFooterLogo.src = isDarkTheme ? yWorksWhite : yWorksBlue
    yWorksFooterLogo.style.height = '30px'
    const yWorksLink = document.createElement('a') as HTMLAnchorElement
    yWorksLink.href = appendCampaign('https://www.yworks.com', 'about')
    yWorksLink.target = '_blank'
    yWorksLink.appendChild(yWorksFooterLogo)
    aboutFooter.appendChild(yWorksLink)

    const aboutText = document.createElement('div')
    aboutText.style.float = 'right'
    aboutText.style.alignItems = 'center'
    aboutText.style.height = '100%'
    aboutText.style.display = 'flex'

    const licenseLink = document.createElement('a')
    licenseLink.href =
      'https://github.com/yWorks/yfiles-jupyter-graphs/blob/master/LICENSE.md'
    licenseLink.target = '_blank'
    licenseLink.text = 'License —'
    licenseLink.style.margin = '0 6px'
    aboutText.appendChild(licenseLink)

    const version = document.createElement('span')
    version.className = 'version'
    // @ts-ignore
    version.innerText = `v${__VERSION__}` // version is provided by webpack as env variable
    aboutText.appendChild(version)

    aboutFooter.appendChild(aboutText)

    root.appendChild(about)
    root.appendChild(aboutFooter)

    return root
  }

  private showContextPane(graphWidget: HTMLElement, id: string) {
    const contextPaneId = `[data-context-pane-id="${id}"]`
    const pane = graphWidget.querySelector(contextPaneId) as HTMLDivElement

    if (!pane) {
      return
    }

    // set active state on the related tab button
    const allTabButtons = Array.from(
      graphWidget.querySelectorAll('[data-btn-pane-id]')
    ) as HTMLDivElement[]
    allTabButtons.forEach((btn) => btn.classList.remove('active'))
    const tabButtonIdSelector = `[data-btn-pane-id="${id}"]`
    const button = graphWidget.querySelector(
      tabButtonIdSelector
    ) as HTMLDivElement
    if (button) {
      button.classList.add('active')
    }

    // hide all panes
    const allPanes = Array.from(
      graphWidget.querySelectorAll('[data-context-pane-id]')
    ) as HTMLDivElement[]
    allPanes.forEach((pane) => {
      pane.style.display = 'none'
    })

    const paneId = pane.getAttribute('data-context-pane-id')

    // show specific pane
    pane.style.display =
      paneId === this.contextPaneConfig[3].id ? 'flex' : 'block'

    // update content in pane
    if (paneId === this.contextPaneConfig[0].id) {
      // switching the pane should fit the entire neighborhood
      this.neighborhoodView.scheduledFitGraphBounds = true
      this.neighborhoodView.scheduleUpdate()
    } else if (paneId === this.contextPaneConfig[1].id) {
      this.updateDataPanel()
    } else if (paneId === this.contextPaneConfig[2].id) {
      this.searchBox.focusInput()
    }
  }

  private static initializeGraphComponent(
    graphComponent: GraphComponent,
    parent: HTMLElement
  ) {
    const mainContainer = document.createElement('div')
    mainContainer.className = 'main-container'

    const gcContainer = document.createElement('div')
    gcContainer.className = 'gc-container'
    const graphComponentDiv = graphComponent.div
    graphComponentDiv.className = 'graphComponent'
    gcContainer.appendChild(graphComponentDiv)

    const watermark = document.createElement('a')
    watermark.className = 'yfiles-watermark'
    watermark.href = `${appendCampaign(
      'https://yworks.com/yfiles-overview',
      'logo'
    )}`
    gcContainer.appendChild(watermark)

    mainContainer.appendChild(gcContainer)
    parent.appendChild(mainContainer)
    return { mainContainer, gcContainer }
  }

  private expandOverview(): void {
    // eslint-disable-next-line
    ;(this.el.querySelector('.overview') as HTMLDivElement).classList.remove(
      'collapsed'
    )
  }

  private collapseOverview(): void {
    // eslint-disable-next-line
    ;(this.el.querySelector('.overview') as HTMLDivElement).classList.add(
      'collapsed'
    )
  }

  private toggleOverview(): void {
    // eslint-disable-next-line
    ;(this.el.querySelector('.overview') as HTMLDivElement).classList.toggle(
      'collapsed'
    )
  }

  private initializeGraphOverview(
    graphOverviewComponent: GraphOverviewComponent,
    parent: HTMLDivElement
  ) {
    graphOverviewComponent.div.setAttribute('style', 'height: 100%')

    const overviewRoot = document.createElement('div') as HTMLDivElement
    overviewRoot.className = 'overview elevation'
    overviewRoot.tabIndex = -1 // make it focusable to not lose focus in widget when clicking

    const header = document.createElement('div')
    header.className = 'header'
    const title = document.createElement('span')
    title.innerText = 'Overview'
    header.addEventListener('click', this.toggleOverview.bind(this))
    header.appendChild(title)

    const graphOverviewContainer = document.createElement('div')
    graphOverviewContainer.className = 'graph-overview-container'
    graphOverviewContainer.appendChild(graphOverviewComponent.div)

    overviewRoot.appendChild(header)
    overviewRoot.appendChild(graphOverviewContainer)
    parent.appendChild(overviewRoot)
  }

  private setupInteractions(graphComponent: GraphComponent) {
    const mode = new GraphEditorInputMode({
      allowAddLabel: false,
      allowAdjustGroupNodeSize: false,
      allowClipboardOperations: false,
      allowCreateBend: false,
      allowCreateEdge: false,
      allowCreateNode: false,
      allowDuplicate: false,
      allowEditLabel: false,
      allowEditLabelOnDoubleClick: false,
      allowGroupingOperations: false,
      allowGroupSelection: false,
      allowPaste: false,
      allowReparentNodes: false,
      allowReparentToNonGroupNodes: false,
      allowReverseEdge: false,
      allowUndoOperations: false,
      allowUngroupSelection: false,
      deletableItems: GraphItemTypes.NONE,
      // suppressing handles effectively turns off
      // - node resizing
      // - edge reconnection
      // - bend movement
      showHandleItems: GraphItemTypes.NONE,
    })
    mode.moveInputMode.enabled = false
    mode.moveLabelInputMode.enabled = false
    mode.marqueeSelectionInputMode.enabled = true
    mode.selectableItems = GraphItemTypes.NODE | GraphItemTypes.EDGE
    mode.marqueeSelectableItems = GraphItemTypes.NODE | GraphItemTypes.EDGE
    mode.moveViewportInputMode = new MoveViewportInputMode({
      priority: 42,
      pressedRecognizer: (eventSource, evt) => {
        const graphComponent = eventSource as GraphComponent
        const isShiftDown = graphComponent.lastInputEvent
          ? (graphComponent.lastInputEvent.modifiers & ModifierKeys.SHIFT) ===
            ModifierKeys.SHIFT
          : false
        return !isShiftDown && MouseEventRecognizers.LEFT_DOWN(eventSource, evt)
      },
    })
    this.setupTooltips(mode)
    this.setupContextView(graphComponent)

    mode.addItemClickedListener((src, args) => {
      const item = args.item
      if (item instanceof ILabel && item.owner) {
        const selection = graphComponent.selection

        // The selection should not be cleared in multi-selection.
        if (args.modifiers !== ModifierKeys.CONTROL) {
          selection.clear()
        }

        const owner = item.owner
        const isOwnerSelected = selection.isSelected(owner)
        graphComponent.selection.setSelected(owner, !isOwnerSelected)
        args.handled = true
      }
    })

    configureIndicatorStyling(graphComponent, mode)

    graphComponent.inputMode = mode
  }

  private setupTooltips(graphEditorInputMode: GraphEditorInputMode) {
    graphEditorInputMode.addQueryItemToolTipListener((sender, evt) => {
      GraphView.createTooltipContentCallback(evt)
    })

    graphEditorInputMode.toolTipItems =
      GraphItemTypes.NODE | GraphItemTypes.EDGE | GraphItemTypes.LABEL
    const mouseHoverInputMode = new AdjustingMouseHoverInputMode()
    mouseHoverInputMode.toolTipLocationOffset = new Point(15, 15)
    mouseHoverInputMode.delay = TimeSpan.fromMilliseconds(500)
    mouseHoverInputMode.duration = TimeSpan.fromSeconds(10)
    mouseHoverInputMode.toolTipParentElement = this.el

    graphEditorInputMode.mouseHoverInputMode = mouseHoverInputMode
  }

  public static createTooltipContentCallback(event: {
    handled: boolean
    toolTip: any
    item: any
  }): void {
    if (event.handled) {
      // Tooltip content has already been assigned -> nothing to do.
      return
    }

    // Use a rich HTML element as tooltip content. Alternatively, a plain string would do as well.
    event.toolTip = GraphView.createTooltipContent(event.item!)

    // Indicate that the tooltip content has been set.
    event.handled = true
  }

  private static createTooltipContent(item: IModelItem): HTMLElement {
    if (item instanceof ILabel) {
      // @ts-ignore
      item = item.owner
    }

    const header = document.createElement('h3')
    header.innerHTML = 'Properties'

    const text = document.createElement('pre')
    text.style.margin = '0'
    // depending on the item, show a different title
    if (INode.isInstance(item)) {
      text.innerHTML = GraphView.getNodeTooltip(item.tag)
    } else if (IEdge.isInstance(item)) {
      text.innerHTML = GraphView.getEdgeTooltip(item.tag)
    } else {
      text.innerHTML = 'not edge or node'
    }

    // build the tooltip container
    const tooltip = document.createElement('p') as HTMLDivElement
    tooltip.className = 'yfiles-jupyter-graphs-tooltip'
    tooltip.appendChild(header)
    tooltip.appendChild(text)
    return tooltip
  }

  /**
   * Adds some meta information to the graph's tag that we utilize for different things, e.g.
   * store from which importer the graph was generated to make certain assumptions in the data-explorer.
   */
  private addGraphMetaData(graph: IGraph): void {
    graph.tag = {
      // @ts-ignore
      version: __VERSION__,
      dataImporter: this.getModelValue<string>('_data_importer'),
      origin: 'yfiles-jupyter-graphs',
    }
  }

  /**
   * @yjs:keep=parentId
   */
  private getGroupNodeIds(nodes: Node_[]): Set<Id> {
    const groupNodeIds = new Set<Id>()
    for (const node of nodes) {
      const parentId = this.getParentId(node)
      if (parentId !== null && !groupNodeIds.has(parentId)) {
        groupNodeIds.add(parentId)
      }
    }
    return groupNodeIds
  }

  /**
   * @yjs:keep=parentId
   */
  private getParentId(node: Node_): Id | null {
    return typeof node.parentId !== 'undefined' ? node.parentId : null
  }

  /**
   * @yjs:keep=start,end,id
   */
  private createGraphBuilder() {
    const builder = new GraphBuilder(this.fullGraph)
    const nodes = [...this.nodes()]
    const groupNodeIds = this.getGroupNodeIds(nodes)
    const nodesSource = builder.createNodesSource({
      data: nodes,
      id: (data) => data.id,
      parentId: (data) => this.getParentId(data),
    })

    nodesSource.nodeCreator.layoutProvider = getNodeLayoutProvider()

    nodesSource.nodeCreator.styleProvider = (dataItem) => {
      const { fill, stroke, shape, image } = parseStyleObject(dataItem)
      if (image) {
        return new ImageNodeStyle({
          image: image,
        })
      }
      return new ShapeNodeStyle({ fill, stroke, shape })
    }
    nodesSource.nodeCreator.addNodeCreatedListener((creator, { item }) => {
      const graph = this.fullGraph
      if (groupNodeIds.has(item.tag.id)) {
        // adopt style properties from the (potentially) mapped node item
        graph.setStyle(item, getGroupStyling(item))

        // position the first label in the GNS header area
        item.labels.forEach((label, idx) => {
          // make sure GNS tab label is centered
          const clone = label.style.clone() as DefaultLabelStyle
          clone.verticalTextAlignment = VerticalTextAlignment.CENTER
          clone.horizontalTextAlignment = HorizontalTextAlignment.CENTER
          graph.setStyle(label, clone)
          graph.setLabelLayoutParameter(
            label,
            idx === 0
              ? new GroupNodeLabelModel().createDefaultParameter()
              : ExteriorLabelModel.SOUTH
          )
        })
      }
    })

    // @ts-ignore
    const nodesLabelsSource = nodesSource.nodeCreator.createLabelsSource({
      data: (data) => (data.label === '' ? [] : [{ ...data }]),
      text: (data) => {
        //@ts-ignore
        return data.label
      },
    })

    const nodesLabelCreator = nodesLabelsSource.labelCreator
    nodesLabelCreator.styleProvider = (dataItem) => {
      return parseLabelObject(dataItem)
    }

    nodesLabelCreator.layoutParameterProvider = (dataItem) => {
      return parseNodeLabelObjectParameter(dataItem)
    }

    configureLabelUpdates(nodesLabelCreator)

    // noinspection JSUnusedGlobalSymbols
    const edgesSource = builder.createEdgesSource({
      data: this.edges(),
      id: (data) => data.id,
      sourceId: (data) => data.start,
      targetId: (data) => data.end,
    })

    const directedModelValue = this.getDirectedValue()
    edgesSource.edgeCreator.styleProvider = (dataItem) => {
      const color = getEdgeStroke(dataItem)
      return new PolylineEdgeStyle({
        stroke: new Stroke(color, getEdgeStrokeThickness(dataItem)),
        targetArrow: getEdgeDirection(directedModelValue, dataItem)
          ? `${color} small triangle`
          : IArrow.NONE,
        smoothingLength: 30,
      })
    }
    //@ts-ignore
    const edgesLabelsSource = edgesSource.edgeCreator.createLabelsSource({
      data: (data: any) => (data.label === '' ? [] : [{ ...data }]),
      text: (data: Edge) => {
        return data.label
      },
    })
    const edgesLabelCreator = edgesLabelsSource.labelCreator
    edgesLabelCreator.styleProvider = (dataItem) => {
      return parseLabelObject(dataItem, true)
    }
    edgesLabelCreator.defaults.layoutParameter =
      FreeEdgeLabelModel.INSTANCE.createDefaultParameter()
    configureLabelUpdates(edgesLabelCreator)

    return builder
  }

  public getDirectedValue(): boolean {
    return this.getModelValue<boolean>('_directed')
  }

  private getContextPaneConfig(): ContextPaneConfig[] {
    return this.getModelValue<ContextPaneConfig[]>('_context_pane_mapping')
  }

  private getNeighborhoodConfig(): {
    maxDistance: number
    selectedNodes: INode[]
  } {
    const neighborhoodConfig =
      this.getModelValue<NeighborhoodConfig>('_neighborhood')
    const selectedNodes: INode[] = []

    const graph = this.graphComponent!.graph
    if (typeof neighborhoodConfig.selected_nodes !== 'undefined') {
      for (const selectedNode of neighborhoodConfig.selected_nodes) {
        const node = graph.nodes.find((n) => n.tag.id === selectedNode)
        if (node) {
          selectedNodes.push(node)
        }
      }
    }

    return {
      maxDistance: neighborhoodConfig.max_distance,
      selectedNodes: selectedNodes,
    }
  }

  private isValidContextId(id: string) {
    return this.contextPaneConfig.findIndex((config) => config.id === id) !== -1
  }

  private getSidebarConfig(): { enabled: boolean; start_with: string } {
    const sidebarConfig = this.getModelValue<SidebarConfig>('_sidebar')
    if (typeof sidebarConfig.enabled === 'undefined') {
      sidebarConfig.enabled = true
    }

    const aboutId = this.contextPaneConfig[this.contextPaneConfig.length - 1].id
    if (
      typeof sidebarConfig.start_with === 'undefined' ||
      !this.isValidContextId(sidebarConfig.start_with)
    ) {
      sidebarConfig.start_with = aboutId
    }

    return sidebarConfig
  }

  private getOverviewConfig(): { enabled: boolean; overview_set: boolean } {
    const overviewConfig = this.getModelValue<OverviewConfig>('_overview')
    if (typeof overviewConfig.enabled === 'undefined') {
      overviewConfig.enabled = true
    }
    if (typeof overviewConfig.overview_set === 'undefined') {
      overviewConfig.overview_set = false
    }
    return overviewConfig
  }

  private getModelValue<T>(key: string): T {
    return this.model.get(key)
  }

  private static limitTopLevelProperties(obj: any): any {
    const maxNumEntries = 8
    let limitedObject = obj
    try {
      if (Object.keys(obj).length > maxNumEntries) {
        limitedObject = Object.fromEntries(
          Object.entries(obj).slice(0, maxNumEntries)
        )
        limitedObject['...'] = 'See more in the data panel'
      }
    } catch (e) {
      // not supported by the client's browser
    }
    return limitedObject
  }

  //@yjs:keep=properties
  private static getNodeTooltip(node: Node_): string {
    return JSON.stringify(
      GraphView.limitTopLevelProperties(node.properties),
      null,
      '  '
    )
  }

  //@yjs:keep=properties
  private static getEdgeTooltip(edge: Edge): string {
    return JSON.stringify(
      GraphView.limitTopLevelProperties(edge.properties),
      null,
      '  '
    )
  }

  private setupContextView(graphComponent: GraphComponent) {
    const selection = graphComponent.selection
    selection.addItemSelectionChangedListener(() => {
      this.updateDataPanel()
      this.onSelectionChanged()
    })
  }

  private updateDataPanel() {
    const selection = this.graphComponent!.selection

    const dataPanel = this.el.querySelector(
      `[data-context-pane-id="${this.contextPaneConfig[1].id}"]`
    ) as HTMLDivElement
    if (!dataPanel || (dataPanel as HTMLDivElement).style.display === 'none') {
      return
    }

    // clear data panel
    while (dataPanel.firstElementChild) {
      dataPanel.removeChild(dataPanel.firstElementChild)
    }

    // create data items from selection
    const items = selection.selectedEdges.concat(selection.selectedNodes)
    if (items.size > 0) {
      this.jsonViewer.addItems(dataPanel, items)
    } else {
      const noSelectionInfo = document.createElement('div')
      noSelectionInfo.innerText =
        'Please select a node or an edge in the diagram to inspect its data.'
      noSelectionInfo.className = 'no-selection'
      noSelectionInfo.style.opacity = '1'
      dataPanel.appendChild(noSelectionInfo)
    }
  }

  /**
   * Called when the graph selection changes, e.g. nodes/edges are selected/deselected.
   */
  private onSelectionChanged(): void {
    const selection = this.graphComponent!.selection

    const noSelectionInfo = this.el.querySelector(
      '.context-pane .no-selection'
    ) as HTMLDivElement
    const hideElements = Array.from(
      this.el.querySelectorAll('.hide-on-no-selection')
    )
    if (
      selection.selectedNodes.size === 0 &&
      selection.selectedEdges.size === 0
    ) {
      noSelectionInfo.style.opacity = '1'
      hideElements.forEach(
        (ele) => ((ele as HTMLDivElement).style.opacity = '0')
      )
    } else {
      noSelectionInfo.style.opacity = '0'
      hideElements.forEach(
        (ele) => ((ele as HTMLDivElement).style.opacity = '1')
      )
    }

    this.highlightGraphItems(
      this.graphComponent!,
      selection.selectedNodes.concat(selection.selectedEdges)
    )
    this.setSelectionPython()
  }

  private setupLevelOfDetailRendering(graphComponent: GraphComponent) {
    const isDirected = this.getDirectedValue()
    graphComponent.graph.nodeDefaults.style = svgNodeStyle
    graphComponent.graph.groupNodeDefaults.labels.layoutParameter =
      new GroupNodeLabelModel().createDefaultParameter()
    graphComponent.graph.edgeDefaults.style = isDirected
      ? svgEdgeStyleDirected
      : svgEdgeStyleUndirected

    const renderingTypesManager = new RenderingTypesManager(graphComponent, 0.5)
    renderingTypesManager.registerZoomChangedListener()
  }

  private initializeHighlights() {
    const highlights = this.model.get('_highlight') as Highlights

    highlights.forEach((data, idx) => {
      const manager = this.initializeHighlightManager(idx)
      this.highlightManagers.push(manager)
      this.highlight(manager, data)
    })
  }

  private initializeHighlightManager(idx: number): ElementIndicatorManager {
    const elementIndicatorManager = new ElementIndicatorManager(
      this.graphComponent!,
      idx,
      false,
      this.getDirectedValue()
    )
    elementIndicatorManager.install(this.graphComponent!)
    return elementIndicatorManager
  }

  private highlight(
    manager: ElementIndicatorManager,
    data: HighlightData
  ): void {
    const graph = this.graphComponent!.graph

    manager.clearHighlights()

    for (const dataNode of data.nodes) {
      const node = graph.nodes.find((n) => n.tag && n.tag.id === dataNode.id)
      if (node) {
        manager.addHighlight(node)
      }
    }
    for (const dataEdge of data.edges) {
      const edge = graph.edges.find((e) => e.tag && e.tag.id === dataEdge.id)
      if (edge) {
        manager.addHighlight(edge)
      }
    }
  }

  private initializeResizeObserver() {
    const observer = new ResizeObserver((entries) => {
      let newSize
      for (const entry of entries) {
        if (entry.contentBoxSize) {
          if (entry.contentBoxSize[0]) {
            newSize = entry.contentBoxSize[0].inlineSize
          } else {
            // legacy path
            // @ts-ignore
            newSize = entry.contentBoxSize.inlineSize
          }
        } else {
          newSize = entry.contentRect.width
        }
      }
      if (newSize) {
        if (newSize < SMALL_WIDGET_BREAKPOINT && !this.smallWidgetLayout) {
          this.smallWidgetLayout = true
          this.el.classList.add('small-widget-layout')
          this.neighborhoodView.fitGraphBounds()
        } else if (
          newSize > SMALL_WIDGET_BREAKPOINT &&
          this.smallWidgetLayout
        ) {
          this.smallWidgetLayout = false
          this.el.classList.remove('small-widget-layout')
          this.neighborhoodView.fitGraphBounds()
        }
      }

      if (!this.initializedWidgetLayout) {
        this.applyOverviewConfig()
        this.initializedWidgetLayout = true
      }
    })
    observer.observe(this.el)
  }

  private applyOverviewConfig() {
    const overviewConfig = this.getOverviewConfig()

    if (!overviewConfig.overview_set) {
      if (this.smallWidgetLayout) {
        this.collapseOverview()
      }
    } else {
      if (overviewConfig.enabled) {
        this.expandOverview()
      } else if (!overviewConfig.enabled) {
        this.collapseOverview()
      }
    }
  }
}
