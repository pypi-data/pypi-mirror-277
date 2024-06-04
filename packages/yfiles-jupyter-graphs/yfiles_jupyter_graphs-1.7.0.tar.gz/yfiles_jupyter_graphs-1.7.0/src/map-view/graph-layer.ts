import {
  DomUtil,
  latLng,
  LatLng,
  LatLngBounds,
  latLngBounds,
  Layer,
  type LayerOptions,
  type LeafletEvent,
  Map as LeafletMap,
} from 'leaflet'
import { GraphComponent, IGraph, INode, Point } from 'yfiles'

/**
 * A Leaflet-layer that contains a {@link GraphComponent}.
 * The {@link GraphComponent} is placed above the map layer,
 * and won't adjust the viewport but calculates the node locations using the geolocations.
 */
export class GraphLayer extends Layer {
  private pane?: HTMLElement
  private mapPane?: HTMLElement

  /**
   * Instantiates the graph layer and initializes the {@link GraphComponent}.
   */
  constructor(
    private readonly graphComponent: GraphComponent,
    private readonly worldMap: LeafletMap,
    private readonly getGeoCoordinates: (
      node: INode
    ) => { lat: number; lng: number } | null,
    options?: LayerOptions
  ) {
    super(options)
  }

  /**
   * @yjs:keep = animate
   */
  onAdd(map: LeafletMap): this {
    this.pane = map.getPane('overlayPane')!
    const parentElement = this.graphComponent.div.parentNode
    if (this.pane && parentElement) {
      parentElement.removeChild(this.graphComponent.div)
      this.pane.appendChild(this.graphComponent.div)
    }
    this.mapPane = map.getPane('mapPane')

    // we'll use the yjg-toolbar buttons instead
    map.removeControl(map.zoomControl)

    map.on(
      'zoom viewreset resize move moveend zoomend',
      this.updateGraphDivHandler.bind(this),
      this
    )
    map.on('zoomstart', this.hideGraphComponent, this)
    map.on('zoomend', this.showGraphComponent, this)
    map.doubleClickZoom.disable()

    // restrict the viewport to the main world map, i.e., prevent infinite world panning
    const southWest = new LatLng(-89.98155760646617, -180)
    const northEast = new LatLng(89.99346179538875, 180)
    const bounds = latLngBounds(southWest, northEast)
    map.setMaxBounds(bounds)
    map.on('drag', () => {
      map.panInsideBounds(bounds, { animate: false })
    })

    // Call updateGraphDiv once to show graph in the initial view
    setTimeout(() => this.updateGraphDiv(map))
    return this
  }

  onRemove(map: LeafletMap): this {
    map.off(
      'zoom viewreset resize move moveend zoomend',
      this.updateGraphDivHandler.bind(this),
      this
    )
    map.off('zoomstart', this.hideGraphComponent, this)
    map.off('zoomend', this.showGraphComponent, this)
    this.pane = undefined
    this.mapPane = undefined
    this.graphComponent.cleanUp()
    this.graphComponent.div.remove()
    return this
  }

  /**
   * Listener for various {@link Map} events, see {@link onAdd} and {@link onRemove}.
   */
  updateGraphDivHandler(evt: LeafletEvent): void {
    this.updateGraphDiv(evt.target as LeafletMap)
  }

  /**
   * Synchronizes the viewport of the map and the {@link GraphComponent}.
   * @yjs:keep = getSize,setPosition,getPosition
   */
  updateGraphDiv(map: LeafletMap): void {
    const graphComponent = this.graphComponent
    // get the size of the map in DOM coordinates
    const mapSize = map.getSize()
    // get the current position of the mapPane
    const globalPos = DomUtil.getPosition(this.mapPane!)
    // calculate the top-left location of our pane
    const topLeft = globalPos.multiplyBy(-1)
    const bottomRight = topLeft.add(mapSize)
    const newSize = bottomRight.subtract(topLeft)

    // resize the graphComponent's div
    graphComponent.div.style.width = `${newSize.x}px`
    graphComponent.div.style.height = `${newSize.y}px`

    // anchor it at the top-left of the screen
    DomUtil.setPosition(this.pane!, topLeft)

    // update the node locations and edge arcs
    this.updateNodeLocations()
  }

  /**
   * Hides the {@link GraphComponent} during zoom.
   */
  hideGraphComponent(): void {
    this.graphComponent.div.style.visibility = 'hidden'
  }

  /**
   * Shows the {@link GraphComponent} after zooming gesture.
   */
  showGraphComponent(): void {
    this.graphComponent.div.style.visibility = 'visible'
  }

  getMapBounds(graph: IGraph, nodes?: INode[]): LatLngBounds | undefined {
    const filteredLocations = (nodes || graph.nodes.toArray())
      .map((n: INode) => this.getGeoCoordinates(n))
      .filter((location) => location !== null)
    if (filteredLocations.length === 0) {
      return undefined
    }
    const mapBounds = filteredLocations.reduce(
      (
        acc: {
          minLat: number
          maxLat: number
          minLng: number
          maxLng: number
        },
        curr: any
      ) => {
        acc.minLat = Math.min(acc.minLat, curr.lat)
        acc.maxLat = Math.max(acc.maxLat, curr.lat)
        acc.minLng = Math.min(acc.minLng, curr.lng)
        acc.maxLng = Math.max(acc.maxLng, curr.lng)
        return acc
      },
      {
        minLat: Number.POSITIVE_INFINITY,
        maxLat: Number.NEGATIVE_INFINITY,
        minLng: Number.POSITIVE_INFINITY,
        maxLng: Number.NEGATIVE_INFINITY,
      }
    )
    return latLngBounds(
      latLng(mapBounds.minLat, mapBounds.minLng),
      latLng(mapBounds.maxLat, mapBounds.maxLng)
    )
  }

  /**
   * @yjs:keep=getPosition,setPosition,getSize
   */
  updateMapSize() {
    // get the size of the map in DOM coordinates
    const mapSize = this.worldMap.getSize()

    // get the current position of the mapPane
    const globalPos = DomUtil.getPosition(this.mapPane!)
    // calculate the top-left location of our pane
    const topLeft = globalPos.multiplyBy(-1)
    const bottomRight = topLeft.add(mapSize)
    const newSize = bottomRight.subtract(topLeft)

    // resize the graphComponent's div
    this.graphComponent.div.style.width = `${newSize.x}px`
    this.graphComponent.div.style.height = `${newSize.y}px`

    // anchor it at the top-left of the screen
    DomUtil.setPosition(this.pane!, topLeft)
    return topLeft
  }

  /**
   * Synchronizes the viewport of the map and the GraphComponent
   * @yjs:keep=getSize,setPosition,getPosition,getCenter
   */
  updateNodeLocations() {
    const topLeft = this.updateMapSize()

    // transform geo-locations and update the node locations
    const graph = this.graphComponent.graph
    graph.nodes.forEach((node: INode) => {
      const coords = this.getGeoCoordinates(node)
      if (coords) {
        // let leaflet calculate the point on the screen from lat/lng
        const layerPoint = Point.from(
          this.worldMap.latLngToLayerPoint(new LatLng(coords.lat, coords.lng))
        )

        // apply the new node location
        graph.setNodeCenter(node, new Point(layerPoint.x, layerPoint.y))
      }
    })

    this.graphComponent.viewPoint = Point.from(topLeft)

    graph.edges.forEach((edge) => graph.clearBends(edge))

    // cause an immediate repaint
    this.graphComponent.updateVisual()
  }

  zoomIn(): void {
    this.worldMap.zoomIn()
  }

  zoomOut(): void {
    this.worldMap.zoomOut()
  }

  /**
   * Adjusts the visible area of the map so the graph elements fit into view.
   * If no parameters are given, all nodes are fitted in the view. If nodes are specified and
   * ignoreCurrentViewport is false, the current viewport is enhanced to include the given nodes.
   * If nodes are specified and ignoreCurrentViewport is true, only the given nodes are fitted into the view.
   * @param graphComponent
   * @param nodes The nodes to include in the viewport.
   * @param ignoreCurrentViewport Whether the current viewport is enhanced to include the given nodes.
   * Only has an effect when nodes are specified.
   * @private
   * @yjs:keep=fitWorld,getCenter,latLngBounds,latLng,fitBounds,padding,animate,maxZoom,updateNodeLocations,getBounds
   */
  fitContent(
    graphComponent: GraphComponent,
    nodes?: INode[],
    ignoreCurrentViewport = true
  ): void {
    const worldMap = this.worldMap
    if (graphComponent.graph.nodes.size === 0) {
      if (nodes) {
        // no nothing in this case because all nodes are filtered
        return
      }
      worldMap.fitWorld()
      return
    }

    const mapBounds = this.getMapBounds(graphComponent.graph, nodes)
    if (!mapBounds) {
      return
    }

    if (nodes) {
      worldMap.fitBounds(
        ignoreCurrentViewport
          ? mapBounds
          : mapBounds.extend(worldMap.getBounds()),
        {
          padding: [100, 100],
          animate: true,
          maxZoom: 10,
        }
      )
    } else {
      worldMap.fitBounds(mapBounds, {
        padding: [100, 100],
        animate: true,
        maxZoom: 10,
      })
    }
    this.updateNodeLocations()
  }
}
