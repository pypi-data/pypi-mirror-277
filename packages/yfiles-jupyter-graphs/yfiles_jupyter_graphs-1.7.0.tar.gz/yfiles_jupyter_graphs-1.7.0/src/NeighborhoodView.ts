import {
  Color,
  ComponentLayout,
  GraphComponent,
  GraphCopier,
  GraphItemTypes,
  GraphViewerInputMode,
  HierarchicLayout,
  ICollection,
  IEdge,
  IEnumerable,
  IGraph,
  ILabel,
  IModelItem,
  INode,
  INodeStyle,
  Insets,
  ItemClickedEventArgs,
  ItemSelectionChangedEventArgs,
  List,
  Mapper,
  MouseWheelBehaviors,
  MutableRectangle,
  Neighborhood,
  NodeStyleDecorationInstaller,
  Point,
  Rect,
  ShapeNodeStyle,
  Stroke,
  StyleDecorationZoomPolicy,
  TimeSpan,
  TraversalDirection,
} from 'yfiles'

import '../css/neighborhood.css'
import { AdjustingMouseHoverInputMode } from './AdjustingMouseHoverInputMode'
import { GraphView } from './widget'
import {
  getSelectionEdgeLabelStyleProvider,
  getSelectionEdgeStyleProvider,
} from './graph-style-configuration'
import { ContentRectViewportLimiter } from './ContentRectViewportLimiter'

/**
 * A widget that can be used together with a {@link NeighborhoodView#graphComponent}
 * or an {@link IGraph} to display the neighborhood of a node.
 */
export default class NeighborhoodView {
  neighborhoodComponent: GraphComponent
  private $graphComponent: GraphComponent | null
  private $sourceGraph: IGraph | null
  private $neighborhoodMode: number
  private $highlightStyle!: INodeStyle
  insets: Insets
  showHighlight: boolean
  autoUpdatesEnabled: boolean
  autoUpdateTimeMillis: number
  clickCallback: any
  // Maps nodes/edges in NeighborhoodComponents' graph to nodes/edges in SourceGraph.
  originalNodes!: Mapper<INode, INode>
  originalEdges!: Mapper<IEdge, IEdge>
  private updateTimerId: number
  scheduledFitGraphBounds = false
  private $selectedNodes: ICollection<INode> | null
  private $selectedEdges: ICollection<IEdge> | null
  private $useSelection: boolean
  private $maxDistance: number
  private readonly $maxSelectedNodesCount: number
  private readonly $maxSelectedEdgesCount: number
  private readonly $graphChangeListener: () => void
  private editListeners!: Map<string, any>
  private toolbar: HTMLDivElement

  /**
   * Creates a new instance of NeighborhoodView.
   */
  constructor(
    private readonly div: HTMLDivElement,
    private readonly graphView: GraphView
  ) {
    const component = new GraphComponent(div)
    component.mouseWheelBehavior = MouseWheelBehaviors.ZOOM
    component.maximumZoom = 3
    component.minimumZoom = 0.1
    component.viewportLimiter = new ContentRectViewportLimiter()
    component.fitGraphBounds()
    this.graphView.blockWheelInteractionWithoutFocus(component.div)
    this.neighborhoodComponent = component

    this.$graphComponent = null
    this.$sourceGraph = null
    this.$neighborhoodMode = NeighborhoodView.MODE_NEIGHBORHOOD

    // Determines if the current root node should be highlighted.
    this.showHighlight = false

    // Checks whether to update the neighborhood view when the graph has been edited.
    this.autoUpdatesEnabled = false

    // The time in milliseconds that updates are scheduled before being executed.
    this.autoUpdateTimeMillis = 100

    // A callback that is invoked on a click in the neighborhood graph with the
    this.clickCallback = null

    // Timer to control the update scheduling.
    this.updateTimerId = -1

    this.$selectedNodes = new List()
    this.$selectedEdges = new List()
    this.$useSelection = true

    this.$maxDistance = 1
    this.$maxSelectedNodesCount = 25
    this.$maxSelectedEdgesCount = 25
    this.showHighlight = true

    // The insets are applied to the graphComponent of this view.
    this.insets = new Insets(5)
    this.autoUpdatesEnabled = true

    this.initializeInputMode()
    this.initializeHighlightStyle()

    this.createEditListeners()
    this.$graphChangeListener = (): void => this.onGraphChanged()

    this.toolbar = this.initializeToolbar(div.parentElement as HTMLDivElement)
  }

  /**
   * Returns the GraphComponent whose graph is displayed in this view.
   */
  get graphComponent(): GraphComponent | null {
    return this.$graphComponent
  }

  /**
   * Specifies the GraphComponent whose graph is displayed in this view.
   */
  set graphComponent(value: GraphComponent | null) {
    this.selectedNodes = null
    this.selectedEdges = null
    if (this.$graphComponent !== null) {
      this.$graphComponent.removeGraphChangedListener(this.$graphChangeListener)
      if (this.useSelection) {
        this.uninstallItemSelectionChangedListener()
      }
    }
    this.$graphComponent = value
    if (this.$sourceGraph !== null) {
      this.uninstallEditListeners()
    }
    if (this.$graphComponent !== null) {
      this.$sourceGraph = this.$graphComponent.graph
      if (this.$sourceGraph !== null) {
        this.installEditListeners()
      }
      this.$graphComponent.addGraphChangedListener(this.$graphChangeListener)
      if (this.useSelection) {
        this.installItemSelectionChangedListener()
      }
    } else {
      this.$sourceGraph = null
    }
  }

  /**
   * Returns the graph that's currently displayed by the neighborhood view.
   */
  get sourceGraph(): IGraph | null {
    return this.$sourceGraph
  }

  /**
   * Specifies the graph that's currently displayed by the neighborhood view.
   */
  set sourceGraph(value: IGraph | null) {
    if (this.$sourceGraph !== null) {
      this.uninstallEditListeners()
    }
    if (this.graphComponent !== null) {
      this.graphComponent.removeGraphChangedListener(this.$graphChangeListener)
      if (this.useSelection) {
        this.uninstallItemSelectionChangedListener()
      }
      this.graphComponent = null
    }
    this.$sourceGraph = value
    if (this.$sourceGraph !== null) {
      this.installEditListeners()
    }
    this.scheduleUpdate()
  }

  /**
   * Returns the method used for neighborhood computation.
   */
  get neighborhoodMode(): number {
    return this.$neighborhoodMode
  }

  /**
   * Specifies the method used for neighborhood computation.
   */
  set neighborhoodMode(value: number) {
    if (this.$neighborhoodMode !== value) {
      this.$neighborhoodMode = value
      this.scheduleUpdate()
    }
  }

  /**
   * Returns the maximum distance for the neighborhood computation.
   */
  get maxDistance(): number {
    return this.$maxDistance
  }

  /**
   * Specifies the maximum distance for the neighborhood computation.
   */
  set maxDistance(value: number) {
    if (this.$maxDistance !== value) {
      this.$maxDistance = value
      this.updateToolbar()
      this.scheduleUpdate()
    }
  }

  /**
   * Returns the maximum number of selected nodes used for neighborhood computation.
   * If the number is exceeded the neighborhood will not be computed.
   */
  get maxSelectedNodesCount(): number {
    return this.$maxSelectedNodesCount
  }

  /**
   * Returns the maximum number of selected edges used for neighborhood computation.
   * If the number is exceeded the neighborhood will not be computed.
   */
  get maxSelectedEdgesCount(): number {
    return this.$maxSelectedEdgesCount
  }

  /**
   * Returns the configurable highlight style. If none is assigned, a default highlight style is used.
   */
  get highlightStyle(): INodeStyle {
    return this.$highlightStyle
  }

  /**
   * Specifies the configurable highlight style. If none is assigned, a default highlight style is used.
   */
  set highlightStyle(value: INodeStyle) {
    this.$highlightStyle = value
    this.installHighlightStyle(this.$highlightStyle)
  }

  /**
   * Gets the nodes whose neighborhoods are shown.
   */
  get selectedNodes(): ICollection<INode> | null {
    return this.$selectedNodes
  }

  /**
   * Sets the nodes whose neighborhoods are shown.
   */
  set selectedNodes(value: ICollection<INode> | null) {
    if (this.$selectedNodes !== value) {
      this.$selectedNodes = value
      this.scheduleUpdate()
    }
  }

  /**
   * Gets the edges whose neighborhoods are shown.
   */
  get selectedEdges(): ICollection<IEdge> | null {
    return this.$selectedEdges
  }

  /**
   * Sets the edges whose neighborhoods are shown.
   */
  set selectedEdges(value: ICollection<IEdge> | null) {
    if (this.$selectedEdges !== value) {
      this.$selectedEdges = value
      this.scheduleUpdate()
    }
  }

  /**
   * Gets whether to automatically synchronize the
   * {@link NeighborhoodView#graphComponent}'s selection to the
   * {@link NeighborhoodView#selectedNodes} of the neighborhood view.
   *
   * The default is <code>true</code>.
   *
   * The view is only updated automatically if {@link NeighborhoodView#autoUpdatesEnabled auto updates}
   * are enabled.
   */
  get useSelection(): boolean {
    return this.$useSelection
  }

  /**
   * Sets whether to automatically synchronize the
   * {@link NeighborhoodView#graphComponent}'s selection to the
   * {@link NeighborhoodView#selectedNodes} of the neighborhood view.
   *
   * The default is <code>true</code>.
   *
   * The view is only updated automatically if {@link NeighborhoodView#autoUpdatesEnabled auto updates}
   * are enabled.
   */
  set useSelection(value: boolean) {
    if (this.$useSelection !== value) {
      this.$useSelection = value
      if (value) {
        if (this.graphComponent !== null) {
          this.selectedNodes = new List(
            this.graphComponent.selection.selectedNodes
          )
          this.selectedEdges = new List(
            this.graphComponent.selection.selectedEdges
          )
        }
        this.installItemSelectionChangedListener()
      } else {
        this.uninstallItemSelectionChangedListener()
      }
    }
  }

  private initializeToolbar(root: HTMLDivElement): HTMLDivElement {
    // reserve space for the toolbar
    this.neighborhoodComponent.contentMargins = new Insets(10, 10, 70, 10)

    const toolbar = document.createElement('div')
    toolbar.className = 'toolbar neighborhood elevation hide-on-no-selection'

    const labeledDepth = document.createElement('div')
    labeledDepth.className = 'depth-container'
    labeledDepth.title = 'Adjust the number of visualized pre- and successors'
    const depthRange = NeighborhoodView.createVerticalRange(
      'depth-slider',
      '130px',
      1,
      5,
      this.$maxDistance,
      (e) => {
        this.maxDistance = parseInt((e.target as HTMLInputElement).value)
      }
    )
    const label = document.createElement('label') as HTMLLabelElement
    label.setAttribute('for', 'depth-slider')
    label.innerText = 'Depth'
    const depthValue = document.createElement('span')
    depthValue.className = 'depth-value'
    depthValue.innerText = `${this.$maxDistance}`

    labeledDepth.appendChild(label)
    labeledDepth.appendChild(depthValue)
    labeledDepth.appendChild(depthRange)

    toolbar.appendChild(labeledDepth)
    root.appendChild(toolbar)
    return toolbar
  }

  private updateToolbar() {
    const depthValue = this.toolbar.querySelector(
      '.depth-value'
    ) as HTMLSpanElement
    depthValue.innerText = `${this.$maxDistance}`
    const slider = this.toolbar.querySelector(
      '.depth-container input'
    ) as HTMLInputElement
    slider.value = `${this.$maxDistance}`
  }

  private static createVerticalRange(
    name: string,
    height: string,
    min: number,
    max: number,
    initialValue: number,
    oninput: (e: Event) => void
  ) {
    const vRange = document.createElement('div')
    vRange.className = name
    const verticalWrapper = document.createElement('div')
    verticalWrapper.className = 'vertical'
    const range = document.createElement('input') as HTMLInputElement
    // noinspection JSSuspiciousNameCombination
    range.style.width = height
    range.type = 'range'
    range.name = 'depth'
    range.min = `${min}`
    range.max = `${max}`
    range.step = '1'
    range.value = `${initialValue}`
    range.name = name
    range.oninput = oninput

    verticalWrapper.appendChild(range)
    vRange.appendChild(verticalWrapper)

    return vRange
  }

  createEditListeners(): void {
    this.editListeners = new Map()
    this.editListeners.set('nodeCreated', () => this.onNodeEdited())
    this.editListeners.set('nodeRemoved', () => this.onNodeRemoved())
    this.editListeners.set(
      'nodeLayoutChanged',
      (source: unknown, node: INode, oldLayout: Rect) => {
        if (
          node.layout.width !== oldLayout.width ||
          node.layout.height !== oldLayout.height
        ) {
          // only react to size changes, since the neighborhood view has its own layout
          this.onNodeEdited()
        }
      }
    )
    this.editListeners.set('nodeStyleChanged', () => this.onNodeEdited())
    this.editListeners.set('edgeCreated', () => this.onEdgeEdited())
    this.editListeners.set('edgeRemoved', () => this.onEdgeRemoved())
    this.editListeners.set('edgePortsChanged', () => this.onEdgeEdited())
    this.editListeners.set('edgeStyleChanged', () => this.onEdgeEdited())
    this.editListeners.set('portAdded', () => this.onPortEdited())
    this.editListeners.set('portRemoved', () => this.onPortEdited())
    this.editListeners.set('portStyleChanged', () => this.onPortEdited())
    this.editListeners.set('labelAdded', () => this.onLabelEdited())
    this.editListeners.set('labelRemoved', () => this.onLabelEdited())
    this.editListeners.set('labelStyleChanged', () => this.onLabelEdited())
    this.editListeners.set('labelTextChanged', () => this.onLabelEdited())

    this.editListeners.set('isGroupNodeChanged', () => this.onItemEdited())
    this.editListeners.set('parentChanged', () => this.onItemEdited())
    this.editListeners.set(
      'itemSelectionChanged',
      (source: unknown, args: ItemSelectionChangedEventArgs<IModelItem>) =>
        this.onItemSelectionChanged(args.item)
    )
  }

  /**
   * Installs listeners such that the neighborhood component is updated if the
   * source graph is edited.
   */
  installEditListeners(): void {
    if (this.sourceGraph === null) {
      return
    }
    this.sourceGraph.addNodeCreatedListener(
      this.editListeners.get('nodeCreated')
    )
    this.sourceGraph.addNodeRemovedListener(
      this.editListeners.get('nodeRemoved')
    )
    this.sourceGraph.addNodeLayoutChangedListener(
      this.editListeners.get('nodeLayoutChanged')
    )
    this.sourceGraph.addNodeStyleChangedListener(
      this.editListeners.get('nodeStyleChanged')
    )
    this.sourceGraph.addEdgeCreatedListener(
      this.editListeners.get('edgeCreated')
    )
    this.sourceGraph.addEdgeRemovedListener(
      this.editListeners.get('edgeRemoved')
    )
    this.sourceGraph.addEdgePortsChangedListener(
      this.editListeners.get('edgePortsChanged')
    )
    this.sourceGraph.addEdgeStyleChangedListener(
      this.editListeners.get('edgeStyleChanged')
    )
    this.sourceGraph.addPortAddedListener(this.editListeners.get('portAdded'))
    this.sourceGraph.addPortRemovedListener(
      this.editListeners.get('portRemoved')
    )
    this.sourceGraph.addPortStyleChangedListener(
      this.editListeners.get('portStyleChanged')
    )
    this.sourceGraph.addLabelAddedListener(this.editListeners.get('labelAdded'))
    this.sourceGraph.addLabelRemovedListener(
      this.editListeners.get('labelRemoved')
    )
    this.sourceGraph.addLabelStyleChangedListener(
      this.editListeners.get('labelStyleChanged')
    )
    this.sourceGraph.addLabelTextChangedListener(
      this.editListeners.get('labelTextChanged')
    )
    this.sourceGraph.addIsGroupNodeChangedListener(
      this.editListeners.get('isGroupNodeChanged')
    )
    this.sourceGraph.addParentChangedListener(
      this.editListeners.get('parentChanged')
    )
  }

  /**
   * Removes the edit listeners.
   */
  uninstallEditListeners(): void {
    if (this.sourceGraph === null) {
      return
    }
    this.sourceGraph.removeNodeCreatedListener(
      this.editListeners.get('nodeCreated')
    )
    this.sourceGraph.removeNodeRemovedListener(
      this.editListeners.get('nodeRemoved')
    )
    this.sourceGraph.removeNodeLayoutChangedListener(
      this.editListeners.get('nodeLayoutChanged')
    )
    this.sourceGraph.removeNodeStyleChangedListener(
      this.editListeners.get('nodeStyleChanged')
    )
    this.sourceGraph.removeEdgeCreatedListener(
      this.editListeners.get('edgeCreated')
    )
    this.sourceGraph.removeEdgeRemovedListener(
      this.editListeners.get('edgeRemoved')
    )
    this.sourceGraph.removeEdgePortsChangedListener(
      this.editListeners.get('edgePortsChanged')
    )
    this.sourceGraph.removeEdgeStyleChangedListener(
      this.editListeners.get('edgeStyleChanged')
    )
    this.sourceGraph.removePortAddedListener(
      this.editListeners.get('portAdded')
    )
    this.sourceGraph.removePortRemovedListener(
      this.editListeners.get('portRemoved')
    )
    this.sourceGraph.removePortStyleChangedListener(
      this.editListeners.get('portStyleChanged')
    )
    this.sourceGraph.removeLabelAddedListener(
      this.editListeners.get('labelAdded')
    )
    this.sourceGraph.removeLabelRemovedListener(
      this.editListeners.get('labelRemoved')
    )
    this.sourceGraph.removeLabelStyleChangedListener(
      this.editListeners.get('labelStyleChanged')
    )
    this.sourceGraph.removeLabelTextChangedListener(
      this.editListeners.get('labelTextChanged')
    )
    this.sourceGraph.removeIsGroupNodeChangedListener(
      this.editListeners.get('isGroupNodeChanged')
    )
    this.sourceGraph.removeParentChangedListener(
      this.editListeners.get('parentChanged')
    )
  }

  onItemEdited(): void {
    if (this.autoUpdatesEnabled) {
      this.scheduleUpdate()
    }
  }

  onNodeEdited(): void {
    if (this.autoUpdatesEnabled) {
      this.scheduleUpdate()
    }
  }

  onNodeRemoved(): void {
    if (this.autoUpdatesEnabled) {
      this.$selectedNodes = new List(
        this.graphComponent!.selection.selectedNodes
      )
      this.scheduleUpdate()
    }
  }

  onEdgeEdited(): void {
    if (this.autoUpdatesEnabled) {
      this.scheduleUpdate()
    }
  }

  private onEdgeRemoved() {
    if (this.autoUpdatesEnabled) {
      this.$selectedEdges = new List(
        this.graphComponent!.selection.selectedEdges
      )
      this.scheduleUpdate()
    }
  }

  onLabelEdited(): void {
    if (this.autoUpdatesEnabled) {
      this.scheduleUpdate()
    }
  }

  onPortEdited(): void {
    if (this.autoUpdatesEnabled) {
      this.scheduleUpdate()
    }
  }

  /**
   * Called whenever the selection changes.
   */
  onItemSelectionChanged(item: IModelItem): void {
    if (this.autoUpdatesEnabled) {
      if (INode.isInstance(item)) {
        this.$selectedNodes = new List(
          this.graphComponent!.selection.selectedNodes
        )
        this.scheduleUpdate()
      } else if (IEdge.isInstance(item)) {
        this.$selectedEdges = new List(
          this.graphComponent!.selection.selectedEdges
        )
        this.scheduleUpdate()
      }
    }
  }

  /**
   * Installs the selection listeners.
   */
  installItemSelectionChangedListener(): void {
    if (this.graphComponent !== null) {
      this.graphComponent.selection.addItemSelectionChangedListener(
        this.editListeners.get('itemSelectionChanged')
      )
    }
  }

  /**
   * Uninstalls the selection listeners.
   */
  uninstallItemSelectionChangedListener(): void {
    if (this.graphComponent !== null) {
      this.graphComponent.selection.removeItemSelectionChangedListener(
        this.editListeners.get('itemSelectionChanged')
      )
    }
  }

  /**
   * Called when the graph property of the source graph is changed.
   */
  onGraphChanged(): void {
    this.sourceGraph = this.graphComponent!.graph
  }

  /**
   * Creates and installs the default highlight style.
   */
  initializeHighlightStyle(): void {
    // create semi transparent orange pen first
    const orangeRed = Color.ORANGE_RED
    const orangePen = new Stroke(orangeRed.r, orangeRed.g, orangeRed.b, 220, 3)
    // freeze it for slightly improved performance
    orangePen.freeze()

    this.highlightStyle = new ShapeNodeStyle({
      shape: 'round-rectangle',
      stroke: orangePen,
      fill: 'transparent',
    })

    // configure the highlight decoration installer
    this.installHighlightStyle(this.highlightStyle)
  }

  /**
   * Installs the given highlight style as node decorator.
   */
  installHighlightStyle(highlightStyle: INodeStyle): void {
    const nodeStyleHighlight = new NodeStyleDecorationInstaller({
      nodeStyle: highlightStyle,
      // that should be slightly larger than the real node
      margins: 5,
      zoomPolicy: StyleDecorationZoomPolicy.VIEW_COORDINATES,
    })
    // register it as the default implementation for all nodes
    const decorator = this.neighborhoodComponent.graph.decorator
    decorator.nodeDecorator.highlightDecorator.setImplementation(
      nodeStyleHighlight
    )

    decorator.edgeDecorator.highlightDecorator.setFactory(
      getSelectionEdgeStyleProvider(this.graphView.getDirectedValue())
    )

    decorator.labelDecorator.highlightDecorator.setFactory(
      getSelectionEdgeLabelStyleProvider()
    )
  }

  /**
   * Initializes the input mode.
   */
  initializeInputMode(): void {
    // We disable focus, selection and marquee selection so the
    // component will display the plain graph without focus and
    // selection boundaries.
    const mode = new GraphViewerInputMode({
      // clickableItems: GraphItemTypes.NODE | GraphItemTypes.EDGE,
      // focusableItems: GraphItemTypes.NONE | GraphItemTypes.EDGE,
      selectableItems: GraphItemTypes.NONE | GraphItemTypes.EDGE,
      marqueeSelectableItems: GraphItemTypes.NONE | GraphItemTypes.EDGE,
      toolTipItems:
        GraphItemTypes.NODE | GraphItemTypes.EDGE | GraphItemTypes.LABEL,
    })

    // Disable collapsing and expanding of groups
    const navigationInputMode = mode.navigationInputMode
    navigationInputMode.allowCollapseGroup = false
    navigationInputMode.allowExpandGroup = false
    navigationInputMode.useCurrentItemForCommands = true
    mode.moveViewportInputMode.enabled = true
    navigationInputMode.enabled = false

    // set up the tooltips
    this.setupTooltips(mode)

    // If an item is clicked, we want the view to show the neighborhood
    // of the clicked node, and invoke the click callback with the original
    // node.
    mode.addItemClickedListener(
      (sender: unknown, args: ItemClickedEventArgs<IModelItem>) => {
        if (this.neighborhoodMode !== NeighborhoodView.MODE_FOLDER_CONTENTS) {
          let item = args.item
          if (item instanceof ILabel && item.owner) {
            item = item.owner
          }

          if (item instanceof INode) {
            const originalNode = this.originalNodes.get(item)
            const selected = new List<INode>()
            selected.add(originalNode!)
            this.selectedNodes = selected
            if (this.clickCallback !== null) {
              this.clickCallback(originalNode)
            }
          } else if (item instanceof IEdge) {
            const originalEdge = this.originalEdges.get(item)
            const selected = new List<IEdge>()
            selected.add(originalEdge!)
            this.selectedEdges = selected
            if (this.clickCallback !== null) {
              this.clickCallback(originalEdge)
            }
          }

          args.handled = true
        }
      }
    )

    this.neighborhoodComponent.inputMode = mode
  }

  private setupTooltips(graphViewerInputMode: GraphViewerInputMode) {
    graphViewerInputMode.addQueryItemToolTipListener((sender, evt) => {
      GraphView.createTooltipContentCallback(evt)
    })

    graphViewerInputMode.toolTipItems =
      GraphItemTypes.NODE | GraphItemTypes.EDGE | GraphItemTypes.LABEL
    const mouseHoverInputMode = new AdjustingMouseHoverInputMode()
    mouseHoverInputMode.toolTipLocationOffset = new Point(15, 15)
    mouseHoverInputMode.delay = TimeSpan.fromMilliseconds(500)
    mouseHoverInputMode.duration = TimeSpan.fromSeconds(10)
    mouseHoverInputMode.toolTipParentElement = this.div

    graphViewerInputMode.mouseHoverInputMode = mouseHoverInputMode
  }

  /**
   * Schedules a call to {@link NeighborhoodView#update}. All consequent calls that
   * happen during the {@link NeighborhoodView#autoUpdateTimeMillis update time} are ignored.
   */
  scheduleUpdate(): void {
    if (this.updateTimerId >= 0) {
      // update is already scheduled
      return
    }
    // schedule an update
    this.updateTimerId = window.setTimeout(() => {
      this.update()
      this.updateTimerId = -1
    }, this.autoUpdateTimeMillis)
  }

  /**
   * Updates the neighborhood view.
   *
   * If {@link NeighborhoodView#autoUpdatesEnabled} is enabled, this method is
   * called automatically after the graph has been edited.
   *
   * Filters the source graph and calculates a layout based on the
   * value set in {@link NeighborhoodView#neighborhoodMode}.
   *
   * @see {@link NeighborhoodView#autoUpdatesEnabled}
   * @see {@link NeighborhoodView#useSelection}
   */
  update(): void {
    const neighborhoodContainer = this.neighborhoodComponent.div.parentElement
    if (
      !neighborhoodContainer ||
      (neighborhoodContainer as HTMLDivElement).style.display === 'none'
    ) {
      return
    }

    const selectedNodes = this.selectedNodes ?? new List()
    const selectedEdges = this.selectedEdges ?? new List()

    this.neighborhoodComponent.graph.clear()
    if (
      this.sourceGraph === null ||
      (selectedNodes.size === 0 && selectedEdges.size === 0) ||
      selectedNodes.size > this.maxSelectedNodesCount ||
      selectedEdges.size > this.maxSelectedEdgesCount
    ) {
      return
    }

    // To be used later as a callback method (avoid duplicate).
    const elementCopiedCallback = (original: IModelItem, copy: IModelItem) => {
      if (INode.isInstance(original)) {
        this.originalNodes.set(copy as INode, original)
        if (selectedNodes.includes(original)) {
          copiedStartNodes.add(copy as INode)
        }
      } else if (IEdge.isInstance(original)) {
        this.originalEdges.set(copy as IEdge, original)
        if (selectedEdges.includes(original)) {
          copiedStartEdges.add(copy as IEdge)
        }
      }
    }

    this.originalNodes = new Mapper<INode, INode>()
    const nodesToCopy = new Set<INode>()
    this.originalEdges = new Mapper<IEdge, IEdge>()

    // Create a list of start nodes.
    const startNodes = selectedNodes

    // Create a list of start nodes that are the source or target nodes of the selected edges.
    const startNodesOfEdges: ICollection<INode> = new List<INode>()
    selectedEdges.forEach((edge: IEdge) => {
      if (edge.sourceNode) {
        startNodesOfEdges.add(edge.sourceNode)
      }
      if (edge.targetNode) {
        startNodesOfEdges.add(edge.targetNode)
      }
    })

    let enumerable: IEnumerable<INode> | null = null
    const copiedStartNodes = new List<INode>()
    const copiedStartEdges = new List<IEdge>()

    if (this.neighborhoodMode !== NeighborhoodView.MODE_FOLDER_CONTENTS) {
      selectedNodes.forEach((node: INode) => {
        nodesToCopy.add(node)
      })

      selectedEdges.forEach((edge: IEdge) => {
        if (edge.sourceNode && !nodesToCopy.has(edge.sourceNode)) {
          nodesToCopy.add(edge.sourceNode)
        }
        if (edge.targetNode && !nodesToCopy.has(edge.targetNode)) {
          nodesToCopy.add(edge.targetNode)
        }
      })

      let direction: TraversalDirection
      switch (this.neighborhoodMode) {
        case NeighborhoodView.MODE_PREDECESSORS:
          // Get predecessors of root node
          direction = TraversalDirection.PREDECESSOR
          break
        case NeighborhoodView.MODE_SUCCESSORS:
          // Get successors of root node
          direction = TraversalDirection.SUCCESSOR
          break
        default:
        case NeighborhoodView.MODE_NEIGHBORHOOD:
          // Get direct and indirect neighbors of root node
          direction = TraversalDirection.UNDIRECTED
          break
      }

      // Get the nodes to be copied, depending on which nodes are selected.
      const resultNodes = new Neighborhood({
        startNodes,
        maximumDistance: this.maxDistance,
        traversalDirection: direction,
      }).run(this.sourceGraph)

      resultNodes.neighbors.forEach((node: INode) => {
        if (!nodesToCopy.has(node)) {
          nodesToCopy.add(node)
        }
      })

      if (this.maxDistance > 1) {
        const resultEdges = new Neighborhood({
          startNodes: startNodesOfEdges,
          maximumDistance: this.maxDistance - 1,
          traversalDirection: direction,
        }).run(this.sourceGraph)

        resultEdges.neighbors.forEach((node: INode) => {
          if (!nodesToCopy.has(node)) {
            nodesToCopy.add(node)
          }
        })
      }

      // Use GraphCopier to copy the nodes inside the neighborhood into the NeighborhoodComponent's graph.
      // Also, create the mapping of the copied nodes to original nodes inside the SourceGraph.
      const graphCopier = new GraphCopier()
      graphCopier.copy(
        this.sourceGraph,
        (item: IModelItem) => !INode.isInstance(item) || nodesToCopy.has(item),
        this.neighborhoodComponent.graph,
        null,
        new Point(0, 0),
        elementCopiedCallback
      )
    } else {
      const foldingView = this.sourceGraph.foldingView!
      if (selectedNodes.size > 1) {
        selectedNodes.forEach((node: INode) => {
          if (this.sourceGraph!.getParent(node) !== null) {
            nodesToCopy.add(foldingView.getMasterItem(node)!)
          }
        })
      }
      if (selectedEdges.size > 1) {
        selectedEdges.forEach((edge: IEdge) => {
          const sourceNode = edge.sourceNode
          const targetNode = edge.targetNode
          if (
            sourceNode &&
            targetNode &&
            this.sourceGraph!.getParent(sourceNode) !== null &&
            this.sourceGraph!.getParent(targetNode) !== null
          ) {
            nodesToCopy.add(foldingView.getMasterItem(sourceNode)!)
            nodesToCopy.add(foldingView.getMasterItem(targetNode)!)
          }
        })
      }

      // Get descendants of root nodes.
      if (this.sourceGraph) {
        const groupingSupport = foldingView.manager.masterGraph.groupingSupport
        const nodesToSelectedEdges: ICollection<INode> = new List()
        selectedEdges.forEach((edge: IEdge) => {
          if (edge.sourceNode) {
            nodesToSelectedEdges.add(edge.sourceNode)
          }
          if (edge.targetNode) {
            nodesToSelectedEdges.add(edge.targetNode)
          }
        })

        selectedNodes.concat(nodesToSelectedEdges).forEach((node: INode) => {
          enumerable = groupingSupport.getDescendants(
            foldingView.getMasterItem(node)
          )

          if (enumerable) {
            enumerable.forEach((descendant: INode) => {
              nodesToCopy.add(descendant)
            })
          }
        })

        // Use GraphCopier to copy the nodes inside the neighborhood into the NeighborhoodComponent's graph.
        // Also, create the mapping of the copied nodes to original nodes inside the SourceGraph.
        // Include only edges that are descendants of the same root node.
        const graphCopier = new GraphCopier()
        graphCopier.copy(
          foldingView.manager.masterGraph,
          (item: IModelItem) => {
            if (IEdge.isInstance(item)) {
              const edge = item
              let intraComponentEdge = false
              selectedNodes.forEach((node: INode) => {
                if (
                  groupingSupport.isDescendant(
                    edge.sourceNode,
                    foldingView.getMasterItem(node)
                  ) &&
                  groupingSupport.isDescendant(
                    edge.targetNode,
                    foldingView.getMasterItem(node)
                  )
                ) {
                  intraComponentEdge = true
                }
              })
              return intraComponentEdge
            }
            return !INode.isInstance(item) || nodesToCopy.has(item)
          },
          this.neighborhoodComponent.graph,
          null,
          new Point(0, 0),
          elementCopiedCallback
        )
      }
    }

    // Layout the neighborhood graph using hierarchic layout.
    if (this.neighborhoodMode === NeighborhoodView.MODE_FOLDER_CONTENTS) {
      if (selectedNodes.size > 1) {
        this.neighborhoodComponent.graph.applyLayout(new ComponentLayout())
      }
    } else {
      this.neighborhoodComponent.graph.applyLayout(
        new HierarchicLayout({
          integratedEdgeLabeling: true,
        })
      )
    }

    // Highlight the root node/edge in the neighborhood graph.
    if (
      this.showHighlight &&
      (copiedStartNodes.size > 0 || copiedStartEdges.size > 0)
    ) {
      const manager = this.neighborhoodComponent.highlightIndicatorManager
      manager.clearHighlights()

      if (copiedStartNodes.size > 0) {
        copiedStartNodes.forEach((startNode: INode) => {
          manager.addHighlight(startNode)
        })
      }

      if (copiedStartEdges.size > 0) {
        copiedStartEdges.forEach((startEdge: IEdge) => {
          manager.addHighlight(startEdge)

          startEdge.labels.forEach((label: ILabel) => {
            manager.addHighlight(label)
          })
        })
      }
    }

    if (this.scheduledFitGraphBounds) {
      // Make the neighborhood graph fit inside the NeighborhoodComponent.
      this.fitGraphBounds()
      this.scheduledFitGraphBounds = false
    } else {
      // keep the zoom level and only focus on the selected items
      this.neighborhoodComponent.updateContentRect(this.insets)
      void this.zoomToSelection(copiedStartNodes.concat(copiedStartEdges))
    }
  }

  zoomToSelection(selectedItems: IEnumerable<IEdge | INode>): Promise<void> {
    if (selectedItems.size === 0) {
      this.fitGraphBounds()
      return Promise.resolve()
    }

    const selectedBounds = new MutableRectangle()
    selectedItems.forEach((item) => {
      if (item instanceof INode) {
        selectedBounds.add(item.layout)
      } else {
        selectedBounds.add(item.sourceNode!.layout)
        selectedBounds.add(item.targetNode!.layout)
      }
    })
    return this.neighborhoodComponent.zoomToAnimated(
      selectedBounds.center,
      this.neighborhoodComponent.zoom
    )
  }

  fitGraphBounds(): void {
    this.neighborhoodComponent.fitGraphBounds(this.insets)
  }

  /**
   * Enumerations that holds the different modes of the NeighborhoodView.
   */
  static get MODE_NEIGHBORHOOD(): number {
    return 0
  }

  static get MODE_PREDECESSORS(): number {
    return 1
  }

  static get MODE_SUCCESSORS(): number {
    return 2
  }

  static get MODE_FOLDER_CONTENTS(): number {
    return 3
  }
}
