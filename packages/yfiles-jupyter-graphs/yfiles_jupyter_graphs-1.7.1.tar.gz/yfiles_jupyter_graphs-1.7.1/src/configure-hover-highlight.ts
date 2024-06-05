import {
  EdgeStyleDecorationInstaller,
  GraphComponent,
  GraphHighlightIndicatorManager,
  GraphInputMode,
  GraphItemTypes,
  HighlightIndicatorManager,
  IArrow,
  ICanvasObjectInstaller,
  IEdge,
  IGraph,
  ILabel,
  IModelItem,
  INode,
  INodeStyle,
  NodeStyleDecorationInstaller,
  PolylineEdgeStyle,
  ShapeNodeShape,
  ShapeNodeStyle,
  StyleDecorationZoomPolicy,
} from 'yfiles'
import {
  getEdgeDirection,
  yfilesSecondaryColor,
} from './graph-style-configuration'

export class GraphHoverHighlightIndicatorManager extends GraphHighlightIndicatorManager {
  getInstaller(item: IModelItem): ICanvasObjectInstaller | null {
    if (item instanceof INode) {
      return GraphHoverHighlightIndicatorManager.getNodeHighlightInstaller(item)
    } else if (item instanceof IEdge) {
      return GraphHoverHighlightIndicatorManager.getEdgeHighlightInstaller(item)
    } else {
      return super.getInstaller(item)
    }
  }

  private static getEdgeHighlightInstaller(
    edge: IEdge
  ): ICanvasObjectInstaller {
    return new EdgeStyleDecorationInstaller({
      edgeStyle: new PolylineEdgeStyle({
        stroke: `3px ${yfilesSecondaryColor}`,
        targetArrow: getEdgeDirection(false, edge.tag)
          ? `${yfilesSecondaryColor} small triangle`
          : IArrow.NONE,
        smoothingLength: 30,
      }),
      zoomPolicy: StyleDecorationZoomPolicy.MIXED,
    })
  }

  private static getNodeHighlightInstaller(
    node: INode
  ): ICanvasObjectInstaller {
    return new NodeStyleDecorationInstaller({
      nodeStyle: new ShapeNodeStyle({
        // the tag of each node contains information about the appropriate shape for the highlight
        shape: GraphHoverHighlightIndicatorManager.getShape(node.style),
        stroke: `3px ${yfilesSecondaryColor}`,
        fill: 'transparent',
      }),
      // the margin from the actual node to its highlight visualization
      margins: 4,
      zoomPolicy: StyleDecorationZoomPolicy.MIXED,
    })
  }

  private static getShape(style: INodeStyle): ShapeNodeShape {
    if (style instanceof ShapeNodeStyle) {
      return style.shape
    }
    return ShapeNodeShape.ROUND_RECTANGLE
  }
}

/**
 * Adds or removes a CSS class to highlight the given item.
 */
function highlightItem(
  graphComponent: GraphComponent,
  highlightManager: HighlightIndicatorManager<IModelItem>,
  item: IModelItem | null,
  highlight: boolean
): void {
  highlightManager.clearHighlights()

  let ownerItem = item
  if (item instanceof ILabel) {
    ownerItem = item.owner
  }

  if (!ownerItem) {
    return
  }

  const graph = graphComponent.graph
  if (highlight) {
    if (ownerItem instanceof IEdge) {
      highlightEdge(graph, highlightManager, ownerItem)
    } else if (ownerItem instanceof INode) {
      highlightNode(graph, highlightManager, ownerItem)
    }
  } else {
    highlightManager.removeHighlight(ownerItem)
  }
}

function highlightEdge(
  graph: IGraph,
  highlightManager: HighlightIndicatorManager<IModelItem>,
  edge: IEdge
): void {
  highlightManager.addHighlight(edge)
  edge.labels.forEach((label) => {
    highlightManager.addHighlight(label)
  })
  highlightManager.addHighlight(edge.sourceNode!)
  highlightManager.addHighlight(edge.targetNode!)
}

function highlightNode(
  graph: IGraph,
  highlightManager: HighlightIndicatorManager<IModelItem>,
  node: INode
): void {
  highlightManager.addHighlight(node)
  const adjacentEdges = graph.edgesAt(node)
  for (const adjacentEdge of adjacentEdges) {
    highlightEdge(graph, highlightManager, adjacentEdge)
    highlightManager.addHighlight(adjacentEdge.opposite(node))
  }
}

export function configureIndicatorStyling(
  graphComponent: GraphComponent,
  inputMode: GraphInputMode
): void {
  const hoverHighlightManager = new GraphHoverHighlightIndicatorManager({
    canvasComponent: graphComponent,
  })

  // show the indicators on hover
  const itemHoverInputMode = inputMode.itemHoverInputMode
  itemHoverInputMode.hoverItems =
    GraphItemTypes.NODE | GraphItemTypes.EDGE | GraphItemTypes.LABEL
  itemHoverInputMode.addHoveredItemChangedListener((_, { item, oldItem }) => {
    highlightItem(graphComponent, hoverHighlightManager, oldItem, false)
    highlightItem(graphComponent, hoverHighlightManager, item, true)
  })
}
