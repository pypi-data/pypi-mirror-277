import {
  Arrow,
  ArrowType,
  CanvasComponent,
  EdgeStyleDecorationInstaller,
  GraphComponent,
  HighlightIndicatorManager,
  ICanvasObjectGroup,
  ICanvasObjectInstaller,
  IEdge,
  INode,
  NodeStyleDecorationInstaller,
  PolylineEdgeStyle,
  ShapeNodeShape,
  ShapeNodeStyle,
  StyleDecorationZoomPolicy,
} from 'yfiles'

export function getHighlightColor(idx: number): string {
  const colors = [
    '#F0C808',
    '#DB3A34',
    '#C7C7A6',
    '#FF6C00',
    '#56926E',
    '#336699',
  ]
  return colors[idx % colors.length]
}

export class ElementIndicatorManager extends HighlightIndicatorManager<
  INode | IEdge
> {
  private readonly nodeInstaller: NodeStyleDecorationInstaller
  private readonly edgeInstaller: EdgeStyleDecorationInstaller
  private readonly indicatorGroup: ICanvasObjectGroup

  constructor(
    canvas: CanvasComponent,
    private highlightIndex: number,
    private showSourceArrow: boolean = false,
    private showTargetArrow: boolean = false
  ) {
    super()
    this.nodeInstaller = new NodeStyleDecorationInstaller({
      nodeStyle: new ShapeNodeStyle({
        stroke: `4px solid ${getHighlightColor(highlightIndex)}`,
        shape: ShapeNodeShape.ELLIPSE,
        fill: null,
      }),
      margins: 3,
      zoomPolicy: StyleDecorationZoomPolicy.MIXED,
    })
    const voidArrow = new Arrow({
      type: ArrowType.NONE,
      cropLength: 5,
    })
    const arrow = new Arrow({
      type: ArrowType.TRIANGLE,
      stroke: `1px solid ${getHighlightColor(highlightIndex)}`,
      fill: getHighlightColor(highlightIndex),
      cropLength: 4,
    })
    this.edgeInstaller = new EdgeStyleDecorationInstaller({
      edgeStyle: new PolylineEdgeStyle({
        stroke: `4px solid ${getHighlightColor(highlightIndex)}`,
        sourceArrow: this.showSourceArrow ? arrow : voidArrow,
        targetArrow: this.showTargetArrow ? arrow : voidArrow,
        smoothingLength: 30,
      }),
      zoomPolicy: StyleDecorationZoomPolicy.MIXED,
    })

    // put each highlight-manager in a separate group behind the labels
    this.indicatorGroup = canvas.contentGroup.addGroup()
    this.indicatorGroup.below(
      (canvas as GraphComponent).graphModelManager.edgeLabelGroup
    )
  }

  protected getCanvasObjectGroup(
    item: INode | IEdge
  ): ICanvasObjectGroup | null {
    return this.indicatorGroup
  }

  getInstaller(item: INode | IEdge): ICanvasObjectInstaller {
    return item instanceof INode ? this.nodeInstaller : this.edgeInstaller
  }
}
