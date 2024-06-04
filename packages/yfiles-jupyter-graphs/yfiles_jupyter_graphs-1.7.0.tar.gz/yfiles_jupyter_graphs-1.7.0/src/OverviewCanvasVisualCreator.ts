import {
  GraphOverviewCanvasVisualCreator,
  IEdge,
  IGraph,
  INode,
  IRenderContext,
} from 'yfiles'

const fullCircle = 2 * Math.PI

/**
 * Custom HTML Canvas rendering for the overview.
 */
export default class OverviewCanvasVisualCreator extends GraphOverviewCanvasVisualCreator {
  constructor(graph: IGraph, private readonly darkMode: boolean) {
    super(graph)
  }

  /**
   * Paints the given node.
   * @param renderContext The render context.
   * @param ctx The HTML canvas rendering context.
   * @param node The node to paint.
   */
  paintNode(
    renderContext: IRenderContext,
    ctx: CanvasRenderingContext2D,
    node: INode
  ): void {
    ctx.fillStyle = 'rgb(128, 128, 128)'
    ctx.strokeStyle = 'rgb(0, 0, 0)'

    const layout = node.layout

    ctx.beginPath()
    ctx.arc(layout.center.x, layout.center.y, layout.width / 2, 0, fullCircle)
    ctx.fill()
    ctx.stroke()
  }

  /**
   * Paints the given edge.
   * @param renderContext The render context.
   * @param ctx The HTML canvas rendering context.
   * @param edge The edge to paint.
   */
  paintEdge(
    renderContext: IRenderContext,
    ctx: CanvasRenderingContext2D,
    edge: IEdge
  ): void {
    ctx.beginPath()
    ctx.moveTo(edge.sourcePort!.location.x, edge.sourcePort!.location.y)
    edge.bends.forEach((bend) => {
      ctx.lineTo(bend.location.x, bend.location.y)
    })
    ctx.lineTo(edge.targetPort!.location.x, edge.targetPort!.location.y)
    ctx.strokeStyle = this.darkMode ? 'rgb(255, 255, 255)' : 'rgb(0, 0, 0)'
    ctx.lineWidth = 1
    ctx.stroke()
  }
}
