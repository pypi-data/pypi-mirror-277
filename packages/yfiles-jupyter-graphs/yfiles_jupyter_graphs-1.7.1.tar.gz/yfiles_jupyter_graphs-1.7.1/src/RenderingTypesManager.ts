import type { GraphComponent, IList, INode } from 'yfiles'
import {
  Color,
  GraphModelManager,
  List,
  Size,
  WebGL2GraphModelManager,
  WebGL2GraphModelManagerRenderMode,
  WebGL2GroupNodeStyle,
  WebGL2IconNodeStyle,
  WebGL2ShapeNodeShape,
  WebGL2ShapeNodeStyle,
  WebGL2Stroke,
} from 'yfiles'

export type RenderingType = 'WebGL2' | 'SVG'

export type RenderingTypeChangedListener = (newValue: RenderingType) => void

class MyWebGL2GraphModelManager extends WebGL2GraphModelManager {
  protected getWebGL2NodeStyle(
    node: INode
  ): WebGL2ShapeNodeStyle | WebGL2IconNodeStyle | WebGL2GroupNodeStyle | null {
    const hasImage = !!node.tag?.styles?.image
    if (hasImage) {
      // return a placeholder for the async loaded image style
      return new WebGL2ShapeNodeStyle(
        WebGL2ShapeNodeShape.ELLIPSE,
        Color.TRANSPARENT,
        WebGL2Stroke.NONE
      )
    }
    return super.getWebGL2NodeStyle(node)
  }
}

/**
 * The {@link RenderingTypesManager} takes care of switching between the two rendering types
 * WebGL2 and SVG.
 * The switching takes place, when a provided threshold is reached:
 * Zoom levels lower than the SVG threshold result in WebGL2 rendering, zoom levels
 * higher than the SVG threshold result in SVG rendering.
 *
 * It also provides listeners, that automatically set the styles for the SVG and
 * WebGL rendering types when new nodes or edges are created.
 */
export default class RenderingTypesManager {
  private readonly listeners: IList<RenderingTypeChangedListener>

  /**
   * Listener for zoom change events. Activates the appropriate
   * rendering method according to the svgThreshold configured,
   * and notifies the rendering changed listeners.
   */
  private readonly zoomChangedListener: () => void

  private svgZoomThreshold: number
  static NODE_COUNT_THRESHOLD = 50

  private readonly $canvasIconRenderingContext: CanvasRenderingContext2D =
    document.createElement('canvas').getContext('2d', {
      willReadFrequently: true,
    }) as CanvasRenderingContext2D

  /**
   * Instantiates the {@link RenderingTypesManager}
   * @param graphComponent the GraphComponent
   * @param svgThreshold the zoom threshold value at which switching between WebGL2 and SVG takes
   *   place
   */
  constructor(
    public readonly graphComponent: GraphComponent,
    svgThreshold = 0.3
  ) {
    this.listeners = new List()

    this.svgZoomThreshold = svgThreshold

    graphComponent.graphModelManager = new MyWebGL2GraphModelManager({
      renderMode: 'web-gl',
    })
    graphComponent.selectionIndicatorManager.enabled = false
    graphComponent.focusIndicatorManager.enabled = false

    this.zoomChangedListener = () => {
      const isWebGLRendering = this.currentRenderingType === 'WebGL2'
      const zoom = this.graphComponent.zoom
      // Make sure to switch only if the threshold is passed
      if (zoom >= this.svgThreshold && isWebGLRendering) {
        this.activateRenderingType('SVG')
        this.fireRenderingTypeChangedEvent()
      } else if (
        !isWebGLRendering &&
        zoom < this.svgThreshold &&
        this.graphComponent.graph.nodes.size >
          RenderingTypesManager.NODE_COUNT_THRESHOLD // switch to WebGL only for larger graphs
      ) {
        this.activateRenderingType('WebGL2')
        this.fireRenderingTypeChangedEvent()
      }
    }

    this.zoomChangedListener()
  }

  get currentRenderingType(): RenderingType {
    const graphModelManager = this.graphComponent
      .graphModelManager as WebGL2GraphModelManager
    return graphModelManager.renderMode ===
      WebGL2GraphModelManagerRenderMode.WEB_GL
      ? 'WebGL2'
      : 'SVG'
  }

  /**
   * Sets a new value for the SVG threshold.
   * @param value The new SVG threshold.
   */
  set svgThreshold(value: number) {
    this.svgZoomThreshold = value
    this.zoomChangedListener()
  }

  /**
   * Gets the value of the SVG threshold.
   * @returns The value of the SVG threshold.
   */
  get svgThreshold(): number {
    return this.svgZoomThreshold
  }

  /**
   * Adds an event listener for zoom changes that switches back and forth between the rendering
   * types when the SVG threshold is passed.
   *
   * @see {@link svgThreshold}
   */
  registerZoomChangedListener(): void {
    this.graphComponent.addZoomChangedListener(this.zoomChangedListener)
    this.zoomChangedListener()
  }

  private unregisterZoomChangedListener(): void {
    this.graphComponent.removeZoomChangedListener(this.zoomChangedListener)
  }

  /**
   * Must be called before instantiating a new {@link RenderingTypesManager},
   * so that the various listeners are unregistered from the {@link GraphComponent}
   */
  public dispose(): void {
    this.unregisterZoomChangedListener()
    this.listeners.clear()
  }

  /**
   * Activates the given rendering type for the graph component of this instance
   * by instantiating and switching to appropriate {@link GraphModelManager}
   * @param type The rendering type.
   */
  activateRenderingType(type: RenderingType): void {
    const gmm = this.graphComponent.graphModelManager as WebGL2GraphModelManager
    if (type === 'WebGL2') {
      gmm.renderMode = WebGL2GraphModelManagerRenderMode.WEB_GL
      const graph = this.graphComponent.graph

      // the image node styles are loaded async, so we need to trigger them explicitly again
      for (const node of graph.nodes) {
        this.replaceImageNodeStyleAsync(node, gmm)
      }
    } else {
      gmm.renderMode = WebGL2GraphModelManagerRenderMode.SVG
    }
  }

  private replaceImageNodeStyleAsync(
    node: INode,
    graphModelManager: WebGL2GraphModelManager
  ) {
    if (
      node.tag &&
      typeof node.tag.styles !== 'undefined' &&
      typeof node.tag.styles.image !== 'undefined'
    ) {
      RenderingTypesManager.getImageData(
        this.$canvasIconRenderingContext,
        node.tag.styles.image,
        node.layout.toSize()
      ).then((imageData: ImageData) => {
        if (this.currentRenderingType === 'WebGL2') {
          // replaces the style once the image has been loaded async
          graphModelManager.setStyle(
            node,
            new WebGL2IconNodeStyle(
              imageData,
              null,
              true,
              WebGL2ShapeNodeShape.ELLIPSE,
              Color.TRANSPARENT,
              WebGL2Stroke.NONE
            )
          )
        }
      })
    }
  }

  private static async getImageData(
    ctx: CanvasRenderingContext2D,
    url: string,
    iconSize: Size
  ): Promise<ImageData> {
    return new Promise((resolve, reject) => {
      // create an Image from the url
      const image = new Image()
      image.onload = () => {
        // render the image into the canvas
        ctx.clearRect(0, 0, iconSize.width, iconSize.height)
        ctx.drawImage(
          image,
          0,
          0,
          image.width,
          image.height,
          0,
          0,
          iconSize.width,
          iconSize.height
        )
        const imageData = ctx.getImageData(
          0,
          0,
          iconSize.width,
          iconSize.height
        )
        resolve(imageData)
      }
      image.crossOrigin = 'Anonymous'
      image.onerror = () => {
        reject('Loading the image failed.')
      }
      image.src = url
    })
  }

  /**
   * Registers a {@link RenderingTypeChangedListener}.
   * @param listener the listener
   */
  addRenderingTypeChangedListener(
    listener: RenderingTypeChangedListener
  ): void {
    this.listeners.push(listener)
  }

  /**
   * Unregisters a {@link RenderingTypeChangedListener}.
   * @param listener the listener
   */
  removeRenderingTypeChangedListener(
    listener: RenderingTypeChangedListener
  ): void {
    this.listeners.remove(listener)
  }

  private fireRenderingTypeChangedEvent(): void {
    for (const listener of this.listeners) {
      listener(this.currentRenderingType)
    }
  }
}
