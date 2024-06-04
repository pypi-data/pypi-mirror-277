import { LatLng, Map as LeafletMap, type MapOptions, TileLayer } from 'leaflet'
import {
  FilteredGraphWrapper,
  GraphComponent,
  GraphViewerInputMode,
  IEdge,
  INode,
  ScrollBarVisibility,
} from 'yfiles'
import 'leaflet/dist/leaflet.css'
import { showToast, straightenEdges } from '../utils'
import { GraphLayer } from './graph-layer'

export class LeafletSupport {
  // holds the hidden nodes by the leaflet map (such that disabling the map only shows the nodes that have been hidden due to missing geo-coords)
  private readonly noGeoCoords = new Set<INode>()

  constructor(
    private readonly graphComponent: GraphComponent,
    private readonly widgetRootElement: HTMLElement,
    private readonly hiddenNodes: Set<INode>
  ) {}

  /**
   * Creates the leaflet container and the GraphLayer which reparents the GraphComponent
   * as its child.
   */
  private initializeLeafletMap(): void {
    const gcContainer =
      this.widgetRootElement.querySelector<HTMLDivElement>('.gc-container')!

    const leafletContainer = document.createElement('div')
    leafletContainer.style.width = '100%'
    leafletContainer.style.height = '100%'
    leafletContainer.setAttribute('data-leaflet-map', '')
    gcContainer.appendChild(leafletContainer)

    // create a Leaflet map that will contain the graphComponent
    const graphLayer = this.createMap(leafletContainer)
    graphLayer.fitContent(this.graphComponent)

    // register button listeners on first initialization
    if (!this.widgetRootElement.hasAttribute('data-leaflet-listening')) {
      this.widgetRootElement.addEventListener('yjg-zoom-in', (e) => {
        graphLayer.zoomIn()
        e.stopPropagation()
      })
      this.widgetRootElement.addEventListener('yjg-zoom-out', (e) => {
        graphLayer.zoomOut()
        e.stopPropagation()
      })
      this.widgetRootElement.addEventListener('yjg-fit-content', (e) => {
        graphLayer.fitContent(this.graphComponent)
        e.stopPropagation()
      })
      this.widgetRootElement.addEventListener('yjg-zoom-to-item', (e) => {
        const { detail } = e as CustomEvent
        if (detail instanceof INode) {
          graphLayer.fitContent(this.graphComponent, [detail])
        } else if (detail instanceof IEdge) {
          graphLayer.fitContent(this.graphComponent, [
            detail.sourceNode!,
            detail.targetNode!,
          ])
        }
        e.stopPropagation()
      })
      gcContainer.setAttribute('data-leaflet-listening', 'true')
    }
  }

  /**
   * @yjs:keep=coordinates
   */
  private getGeoCoordinates(node: INode): { lat: number; lng: number } | null {
    const position = node.tag.coordinates
    return position ? { lat: position[0], lng: position[1] } : null
  }

  /**
   * Creates a Leaflet map and adds a graph layer which contains a {@link GraphComponent}.
   * @yjs:keep = control
   */
  private createMap(
    leafletContainer: HTMLElement,
    leafletOptions?: MapOptions
  ): GraphLayer {
    // use openstreetmap tiles for this demo:
    // create the tile layer with the correct attribution
    const osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    const osmAttrib =
      'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'

    // create the map
    const worldMap = new LeafletMap(leafletContainer, leafletOptions)
    worldMap.setView(new LatLng(15.538, 16.523), 3)
    worldMap.addLayer(
      new TileLayer(osmUrl, {
        minZoom: 1,
        maxZoom: 18,
        attribution: osmAttrib,
      })
    )

    // now create the GraphLayer
    const graphLayer = new GraphLayer(
      this.graphComponent,
      worldMap,
      this.getGeoCoordinates
    )
    // and add it to the map
    worldMap.addLayer(graphLayer)

    return graphLayer
  }

  private resetFilteringState() {
    for (const node of this.noGeoCoords) {
      this.hiddenNodes.delete(node)
      this.noGeoCoords.delete(node)
    }
  }

  private filterUnmappedNode(node: INode) {
    this.noGeoCoords.add(node)
    this.hiddenNodes.add(node)
  }

  toggleMapOverlay(showMap: boolean): void {
    const gcContainer =
      this.widgetRootElement.querySelector<HTMLDivElement>('.gc-container')!
    const leafletMap =
      this.widgetRootElement.querySelector<HTMLDivElement>('[data-leaflet-map]')

    const inputMode = this.graphComponent.inputMode as GraphViewerInputMode

    const filteredGraphWrapper = this.graphComponent
      .graph as FilteredGraphWrapper
    const fullGraph = filteredGraphWrapper.wrappedGraph!

    if (showMap && !leafletMap) {
      straightenEdges(this.graphComponent)

      this.resetFilteringState()
      for (const node of fullGraph.nodes) {
        const geoCoords = this.getGeoCoordinates(node)
        // Explicitly check for undefined and null here
        // eslint-disable-next-line eqeqeq
        if (!geoCoords || geoCoords.lat == null || geoCoords.lng == null) {
          this.filterUnmappedNode(node)
        }
      }
      filteredGraphWrapper.nodePredicateChanged()

      this.graphComponent.zoom = 1
      this.graphComponent.autoDrag = false
      this.graphComponent.horizontalScrollBarPolicy = 'never'
      this.graphComponent.verticalScrollBarPolicy = 'never'
      this.graphComponent.sizeChangedDetection = 'timer'
      this.graphComponent.mouseWheelBehavior = 'none'
      inputMode.moveViewportInputMode.enabled = false
      inputMode.marqueeSelectionInputMode.enabled = false

      this.initializeLeafletMap()

      const gcContainer =
        this.widgetRootElement.querySelector<HTMLDivElement>('.gc-container')!
      if (this.graphComponent.graph.nodes.size === 0) {
        showToast(
          gcContainer,
          'No geo-coordinates found. Please specify a coordinates mapping function and ensure that it maps to the correct data.',
          undefined,
          true
        )
      } else if (this.noGeoCoords.size > 0) {
        showToast(
          gcContainer,
          'Some nodes could not be placed on the map because they could not be mapped to a geolocation.',
          undefined,
          true
        )
      }

      this.widgetRootElement.classList.add('map-view')
    } else if (!showMap) {
      if (leafletMap) {
        leafletMap.parentElement?.removeChild(leafletMap)
      }
      gcContainer.prepend(this.graphComponent.div)

      this.graphComponent.autoDrag = true
      this.graphComponent.verticalScrollBarPolicy =
        ScrollBarVisibility.AS_NEEDED_DYNAMIC
      this.graphComponent.horizontalScrollBarPolicy =
        ScrollBarVisibility.AS_NEEDED_DYNAMIC
      this.graphComponent.sizeChangedDetection = 'sensor'
      this.graphComponent.mouseWheelBehavior = 'zoom'
      inputMode.moveViewportInputMode.enabled = true
      inputMode.marqueeSelectionInputMode.enabled = true

      this.resetFilteringState()
      filteredGraphWrapper.nodePredicateChanged()

      this.widgetRootElement.classList.remove('map-view')
    }

    this.widgetRootElement.dispatchEvent(
      new Event('yjg-invalidate-search-results')
    )
  }

  static isInMapMode(widgetRootElement: Element): boolean {
    return !!widgetRootElement.querySelector<HTMLDivElement>(
      '[data-leaflet-map]'
    )
  }
}
