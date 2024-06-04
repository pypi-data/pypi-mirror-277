import {
  ImageNodeStyleRenderer,
  IRenderContext,
  SvgVisual,
  Visual,
} from 'yfiles'

export default class AspectRatioImageNodeStyleRenderer extends ImageNodeStyleRenderer {
  createVisual(context: IRenderContext): Visual | null {
    const visual = super.createVisual(context) as SvgVisual
    visual.svgElement.setAttribute('preserveAspectRatio', 'xMidYMid')
    return visual
  }
}
