/**
 * IMPORTANT:
 * ==========
 *
 * The yfiles imports here **MUST** be module split because they are loaded in the worker as well.
 *
 * This is necessary for the jupyter labextension bundle to work correctly. For whatever reason, loading from yfiles
 * does NOT work in the labextension bundle. The 'jupyter labextension build' internally uses Webpack 5 with Module
 * Federation. Maybe it is misconfigured somehow or there is a problem regarding Module Federation with this approach.
 */
import {
  ChainSubstructureStyle,
  ComponentArrangementStyles,
  ComponentLayout,
  CycleSubstructureStyle,
  EdgeBundleDescriptor,
  EdgeRouterEdgeRoutingStyle,
  EdgeRouterScope,
  GenericLabeling,
  ILayoutAlgorithm,
  LabelAngleReferences,
  LabelPlacements,
  LayoutOrientation,
  OrganicLayoutStarSubstructureStyle,
  ParallelSubstructureStyle,
  PortCalculator,
  PreferredPlacementDescriptor,
  SequentialLayout,
  TreeLayoutEdgeRoutingStyle,
  ParallelEdgeRouter,
} from 'yfiles/layout-core'
import {
  CircularLayoutData,
  EdgeRouterData,
  GenericLayoutData,
  HierarchicLayoutData,
  LayoutData,
  LayoutGraphAdapter,
  OrganicEdgeRouterData,
  OrthogonalLayoutData,
  RadialLayoutData,
  TreeLayoutData,
} from 'yfiles/view-layout-bridge'
import {
  CircularLayout,
  CircularLayoutStyle,
  OrganicLayout,
} from 'yfiles/layout-organic'
import {
  ComponentArrangementPolicy,
  GroupCompactionPolicy,
  HierarchicLayout,
  HierarchicLayoutEdgeRoutingStyle,
  HierarchicLayoutLayeringStrategy,
  HierarchicLayoutRoutingStyle,
  NodeLabelMode,
  RecursiveEdgeStyle,
  SimplexNodePlacer,
} from 'yfiles/layout-hierarchic'
import { ILabel } from 'yfiles/view-component'
import {
  OrthogonalLayout,
  OrthogonalLayoutStyle,
} from 'yfiles/layout-orthogonal'
import { RadialLayout } from 'yfiles/layout-radial'
import {
  DefaultNodePlacer,
  TreeLayout,
  TreeReductionStage,
} from 'yfiles/layout-tree'
import { OrganicEdgeRouter } from 'yfiles/router-other'
import { EdgeRouter } from 'yfiles/router-polyline'

export type LayoutStyle = {
  title: string
  key: string
  layout?: ILayoutAlgorithm
  layoutData?: LayoutData | null
}

export type LayoutStyles = {
  [key: string]: LayoutStyle
}

export type LayoutTuple = {
  layout: ILayoutAlgorithm
  layoutData: LayoutData | null
}

/**
 * Maximum duration of 5 minutes.
 */
const MAXIMUM_DURATION = 1000 * 60 * 5

function createCircularLayout(): LayoutTuple {
  const layout = new CircularLayout({
    considerNodeLabels: true,
    labeling: new GenericLabeling({
      placeEdgeLabels: true,
      placeNodeLabels: false,
    }),
    labelingEnabled: true,
    layoutStyle: CircularLayoutStyle.BCC_COMPACT,
  })
  const ebc = layout.edgeBundling
  ebc.defaultBundleDescriptor = new EdgeBundleDescriptor({ bundled: true })
  return { layout, layoutData: new CircularLayoutData() }
}

function createHierarchicLayout(): LayoutTuple {
  const layout = new HierarchicLayout()

  const np = layout.nodePlacer as SimplexNodePlacer
  np.barycenterMode = true
  np.straightenEdges = false
  np.groupCompactionStrategy = GroupCompactionPolicy.MAXIMAL
  np.nodeCompaction = false

  layout.maximumDuration = MAXIMUM_DURATION

  layout.componentLayoutEnabled = false
  layout.nodeToNodeDistance = 30
  layout.nodeToEdgeDistance = 15
  layout.edgeToEdgeDistance = 15
  layout.minimumLayerDistance = 10
  layout.layoutOrientation = LayoutOrientation.TOP_TO_BOTTOM
  layout.considerNodeLabels = true
  layout.fromScratchLayeringStrategy =
    HierarchicLayoutLayeringStrategy.HIERARCHICAL_OPTIMAL
  layout.componentArrangementPolicy = ComponentArrangementPolicy.TOPMOST
  layout.recursiveGroupLayering = false
  layout.backLoopRouting = false
  layout.backLoopRoutingForSelfLoops = false
  layout.integratedEdgeLabeling = true

  const eld = layout.edgeLayoutDescriptor
  eld.routingStyle = new HierarchicLayoutRoutingStyle(
    HierarchicLayoutEdgeRoutingStyle.ORTHOGONAL
  )
  eld.minimumDistance = 15
  eld.minimumLength = 20
  eld.minimumSlope = 0.25
  eld.sourcePortOptimization = false
  eld.targetPortOptimization = false
  eld.recursiveEdgeStyle = RecursiveEdgeStyle.OFF

  const nld = layout.nodeLayoutDescriptor
  nld.minimumDistance = Math.min(
    layout.nodeToNodeDistance,
    layout.nodeToEdgeDistance
  )
  nld.minimumLayerHeight = 0
  nld.layerAlignment = 0.5
  nld.nodeLabelMode = NodeLabelMode.CONSIDER_FOR_DRAWING

  return { layout, layoutData: new HierarchicLayoutData() }
}

function createOrganicLayout(): LayoutTuple {
  const layout = new OrganicLayout()

  ;(layout.componentLayout as ComponentLayout).style =
    ComponentArrangementStyles.MULTI_ROWS

  layout.minimumNodeDistance = 50

  layout.maximumDuration = MAXIMUM_DURATION
  layout.considerNodeSizes = true
  layout.considerNodeLabels = true
  layout.integratedEdgeLabeling = true

  layout.cycleSubstructureStyle = CycleSubstructureStyle.CIRCULAR
  layout.chainSubstructureStyle = ChainSubstructureStyle.NONE
  layout.parallelSubstructureStyle = ParallelSubstructureStyle.RADIAL
  layout.starSubstructureStyle = OrganicLayoutStarSubstructureStyle.RADIAL

  const edgeRouter = layout.parallelEdgeRouter as ParallelEdgeRouter
  edgeRouter.joinEnds = true
  edgeRouter.lineDistance = 40

  const genericLabeling = new GenericLabeling()
  genericLabeling.placeEdgeLabels = true
  genericLabeling.placeNodeLabels = false
  genericLabeling.reduceAmbiguity = false
  layout.labeling = genericLabeling
  layout.labelingEnabled = true

  const descriptor = new PreferredPlacementDescriptor({
    sideOfEdge: LabelPlacements.ON_EDGE,
    placeAlongEdge: LabelPlacements.AT_CENTER,
    angle: 0,
    angleReference: LabelAngleReferences.RELATIVE_TO_EDGE_FLOW,
  })

  const genericLayoutData = new GenericLayoutData({
    labelItemMappings: [
      [
        LayoutGraphAdapter.EDGE_LABEL_LAYOUT_PREFERRED_PLACEMENT_DESCRIPTOR_DP_KEY,
        (label: ILabel) => descriptor,
      ],
    ],
  })

  return { layout, layoutData: genericLayoutData }
}

function createOrthogonalLayout(): LayoutTuple {
  const layout = new OrthogonalLayout()

  ;(layout.componentLayout as ComponentLayout).style =
    ComponentArrangementStyles.MULTI_ROWS

  layout.layoutStyle = OrthogonalLayoutStyle.NORMAL

  const eld = layout.edgeLayoutDescriptor
  eld.minimumSegmentLength = 10

  layout.maximumDuration = MAXIMUM_DURATION
  layout.gridSpacing = 25
  layout.edgeLengthReduction = true
  layout.crossingReduction = true
  layout.optimizePerceivedBends = true
  layout.alignDegreeOneNodes = true
  layout.randomization = true
  layout.faceMaximization = false
  layout.fromSketchMode = false
  layout.parallelEdgeRouterEnabled = false
  layout.integratedEdgeLabeling = true
  layout.considerNodeLabels = true

  return { layout, layoutData: new OrthogonalLayoutData() }
}

function createRadialLayout(): LayoutTuple {
  const layout = new RadialLayout({
    considerNodeLabels: true,
    labeling: new GenericLabeling({
      placeEdgeLabels: true,
      placeNodeLabels: false,
    }),
    labelingEnabled: true,
  })

  return { layout, layoutData: new RadialLayoutData() }
}

function createTreeLayout(): LayoutTuple {
  const layout = new TreeLayout({
    multiParentAllowed: true,
  })

  const dnp = new DefaultNodePlacer()
  dnp.horizontalDistance = 20
  dnp.verticalDistance = 40
  dnp.routingStyle = TreeLayoutEdgeRoutingStyle.POLYLINE
  dnp.verticalAlignment = 0.5

  layout.defaultNodePlacer = dnp

  layout.considerNodeLabels = true
  layout.integratedEdgeLabeling = true

  const stage = new TreeReductionStage(layout)
  stage.multiParentAllowed = true

  stage.nonTreeEdgeRouter = new OrganicEdgeRouter()
  stage.nonTreeEdgeSelectionKey = OrganicEdgeRouter.AFFECTED_EDGES_DP_KEY

  stage.nonTreeEdgeLabelSelectionKey = 'NON_TREE_EDGE_LABEL_KEY'
  stage.nonTreeEdgeLabelingAlgorithm = new GenericLabeling({
    affectedLabelsDpKey: 'NON_TREE_EDGE_LABEL_KEY',
  })

  return { layout: stage, layoutData: new TreeLayoutData() }
}

function createOrthogonalRouter(): LayoutTuple {
  const router = new EdgeRouter({
    considerNodeLabels: true,
    integratedEdgeLabeling: true,
  })

  router.maximumDuration = MAXIMUM_DURATION

  const eld = router.defaultEdgeLayoutDescriptor
  eld.routingStyle = EdgeRouterEdgeRoutingStyle.ORTHOGONAL
  const penaltySettings = eld.penaltySettings
  penaltySettings.bendPenalty = 3
  penaltySettings.edgeCrossingPenalty = 1

  router.scope = EdgeRouterScope.ROUTE_ALL_EDGES

  return {
    layout: new PortCalculator(router),
    layoutData: new EdgeRouterData(),
  }
}

function createOrganicRouter(): LayoutTuple {
  const router = new OrganicEdgeRouter()

  router.routeAllEdges = true
  const algorithm = new SequentialLayout()
  algorithm.appendLayout(router)
  algorithm.appendLayout(new GenericLabeling({ placeNodeLabels: false }))

  return { layout: algorithm, layoutData: new OrganicEdgeRouterData() }
}

export const LAYOUT_ALGORITHMS: LayoutStyles = {
  circular: {
    key: 'circular',
    title: 'Circular Layout',
    ...createCircularLayout(),
  },
  hierarchic: {
    key: 'hierarchic',
    title: 'Hierarchic Layout',
    ...createHierarchicLayout(),
  },
  organic: {
    key: 'organic',
    title: 'Static',
    ...createOrganicLayout(),
  },
  interactive_organic: {
    key: 'interactive_organic',
    title: 'Interactive',
  },
  orthogonal: {
    key: 'orthogonal',
    title: 'Orthogonal Layout',
    ...createOrthogonalLayout(),
  },
  radial: { key: 'radial', title: 'Radial Layout', ...createRadialLayout() },
  tree: { key: 'tree', title: 'Tree Layout', ...createTreeLayout() },
  orthogonal_edge_router: {
    key: 'orthogonal_edge_router',
    title: 'Orthogonal',
    ...createOrthogonalRouter(),
  },
  organic_edge_router: {
    key: 'organic_edge_router',
    title: 'Organic',
    ...createOrganicRouter(),
  },
  map: {
    key: 'map',
    title: 'Geospatial Layout',
  },
}
