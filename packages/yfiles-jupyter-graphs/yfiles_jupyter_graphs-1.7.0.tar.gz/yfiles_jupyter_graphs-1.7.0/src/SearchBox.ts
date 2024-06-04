import '../css/searchbox.css'
import {
  FilteredGraphWrapper,
  GraphComponent,
  IEdge,
  IEnumerable,
  IGraph,
  IModelItem,
  INode,
  Rect,
} from 'yfiles'
import { mdiCheckboxBlankCircle, mdiEye, mdiRayStartArrow } from '@mdi/js'
import { edgeStroke, nodeFill } from './graph-style-configuration'
import { createIconSvg, createMdiIconSpan } from './utils'
import { LeafletSupport } from './map-view/leaflet-support'

const SELECTED_ITEM_CSS_CLASS = 'selected'

type ResultItem = {
  item: INode | IEdge
  key?: string // the key if hit is in a key-value pair
  value: string
  type: ResultItemType
  isVisible: boolean // whether it is visible or filtered in the current graph
}

enum ResultItemType {
  NODE,
  EDGE,
}

export class SearchBox {
  private graph: IGraph
  private readonly searchInput: HTMLInputElement
  private selectedItemIndex: number
  private selectedItemElement: HTMLLIElement | undefined
  private readonly dropDownList: HTMLUListElement
  private matchingItems: ResultItem[]
  private queryTimer: number | null = null

  /**
   * Creates a search input field within the <code>parentElement</code>, which allows to search in the passed graph.
   * While entering the search string a suggestion drop down list will be shown.
   * This constructor allows customizing of the search behavior by the given callbacks.
   * @param widgetRootElement The root element of the widget
   * @param parentElement The parent DOM Element the search field will be created in.
   * @param graphComponent The graph control of the graph to search in.
   */
  constructor(
    private readonly widgetRootElement: HTMLElement,
    parentElement: HTMLElement,
    private graphComponent: GraphComponent
  ) {
    // Searchbox will search the full Graph if it is filtered.
    if (graphComponent.graph instanceof FilteredGraphWrapper) {
      this.graph = graphComponent.graph.wrappedGraph!
    } else {
      this.graph = graphComponent.graph
    }

    const div = window.document.createElement('div')
    div.setAttribute('class', 'search')
    this.searchInput = document.createElement('input')
    this.searchInput.setAttribute('type', 'search')
    this.searchInput.setAttribute('placeholder', 'Search graph items...')
    this.searchInput.addEventListener('input', this.onSearchInput.bind(this))
    this.searchInput.addEventListener('keydown', (evt: KeyboardEvent) =>
      this.onKeyDown(evt)
    )
    this.dropDownList = window.document.createElement('ul')
    this.dropDownList.setAttribute('class', 'results')

    div.appendChild(this.searchInput)
    div.appendChild(this.dropDownList)
    parentElement.appendChild(div)

    this.widgetRootElement.addEventListener(
      'yjg-invalidate-search-results',
      (e) => {
        e.stopPropagation()
        this.invalidateSearchResults()
      }
    )
  }

  /**
   * Focus the input field.
   */
  public focusInput(): void {
    this.searchInput.focus()
    this.searchInput.select()
  }

  /**
   * Gets called on the search input event (debounced).
   */
  private onSearchInput(): void {
    if (this.queryTimer !== null) {
      return
    }
    this.queryTimer = setTimeout(() => {
      this.invalidateSearchResults()
      this.queryTimer = null
    }, 100)
  }

  clearSearch(): void {
    this.searchInput.value = ''
    this.populateResultContainer('', [])
  }

  /**
   * Re-evaluates the search input string and populates the results
   */
  invalidateSearchResults() {
    const searchString = this.searchInput.value.toLowerCase()
    this.matchingItems = this.searchGraph(searchString)
    this.populateResultContainer(searchString, this.matchingItems)
  }

  /**
   * Gets called on the search input keydown event.
   * @param {KeyboardEvent} evt The keyboard event.
   */
  private onKeyDown(evt: KeyboardEvent): void {
    if (evt.which === 40 && this.matchingItems.length > 0) {
      // down
      evt.preventDefault()
      if (
        this.selectedItemIndex === -1 ||
        this.selectedItemIndex === this.matchingItems.length - 1
      ) {
        this.selectFirst()
      } else {
        this.selectNext()
      }
    } else if (evt.which === 38 && this.matchingItems.length > 0) {
      // up
      evt.preventDefault()
      if (this.selectedItemIndex === -1 || this.selectedItemIndex === 0) {
        this.selectLast()
      } else {
        this.selectPrevious()
      }
    } else if (evt.which === 34 && this.matchingItems.length > 0) {
      // pdown
      evt.preventDefault()
      this.selectLast()
    } else if (evt.which === 33 && this.matchingItems.length > 0) {
      // pgup
      evt.preventDefault()
      this.selectFirst()
    } else if (evt.which === 27) {
      // esc
      evt.preventDefault()
      this.clearSearch()
    } else if (evt.which === 13 && this.selectedItemIndex >= 0) {
      // enter
      evt.preventDefault()
      this.selectItem(this.matchingItems[this.selectedItemIndex].item)
    }
  }

  /**
   * Selects the first element of the suggestion list.
   */
  private selectFirst(): void {
    this.removeSelectedCssClass()
    this.selectedItemElement = this.dropDownList.firstChild as HTMLLIElement
    this.selectedItemElement.className = SELECTED_ITEM_CSS_CLASS
    this.selectedItemIndex = 0
    this.scrollUpToSelectedItem()
  }

  /**
   * Selects the last element of the suggestion list.
   */
  private selectLast(): void {
    this.removeSelectedCssClass()
    this.selectedItemElement = this.dropDownList.lastChild as HTMLLIElement
    this.selectedItemElement.className = SELECTED_ITEM_CSS_CLASS
    this.selectedItemIndex = this.matchingItems.length - 1
    this.scrollDownToSelectedItem()
  }

  /**
   * Selects the previous element of the suggestion list.
   */
  private selectPrevious(): void {
    this.removeSelectedCssClass()
    if (this.selectedItemElement) {
      this.selectedItemElement = this.selectedItemElement
        .previousSibling as HTMLLIElement
      this.selectedItemElement.className = SELECTED_ITEM_CSS_CLASS
      this.selectedItemIndex--
      this.scrollUpToSelectedItem()
    }
  }

  /**
   * Selects the next element of the suggestion list.
   */
  private selectNext(): void {
    this.removeSelectedCssClass()
    if (this.selectedItemElement) {
      this.selectedItemElement = this.selectedItemElement
        .nextSibling as HTMLLIElement
      this.selectedItemElement.className = SELECTED_ITEM_CSS_CLASS
      this.selectedItemIndex++
      this.scrollDownToSelectedItem()
    }
  }

  private removeSelectedCssClass(): void {
    if (this.selectedItemElement) {
      this.selectedItemElement.className = ''
    }
  }

  private selectResultItem(element: HTMLLIElement) {
    this.removeSelectedCssClass()
    this.selectedItemElement = element
    element.className = SELECTED_ITEM_CSS_CLASS
    this.selectedItemIndex = -1
  }

  /**
   * Scrolls up if necessary.
   */
  private scrollUpToSelectedItem(): void {
    if (this.selectedItemElement) {
      this.dropDownList.scrollTop = Math.min(
        this.selectedItemElement.offsetTop,
        this.dropDownList.scrollTop
      )
    }
  }

  /**
   * Scrolls down if necessary.
   */
  private scrollDownToSelectedItem(): void {
    if (this.selectedItemElement) {
      this.dropDownList.scrollTop = Math.max(
        this.dropDownList.scrollTop,
        Math.max(
          this.selectedItemElement.offsetTop,
          this.dropDownList.scrollTop
        ) -
          this.dropDownList.clientHeight +
          this.selectedItemElement.offsetHeight
      )
    }
  }

  /**
   * Populates the suggestion list with items using the createItemElement callback for each node.
   * @param searchString The search string used.
   * @param matchingItems The nodes result list.
   */
  private populateResultContainer(
    searchString: string,
    matchingItems: ResultItem[]
  ) {
    this.matchingItems = matchingItems
    while (this.dropDownList.lastChild) {
      this.dropDownList.removeChild(this.dropDownList.lastChild)
    }

    for (const resultItem of matchingItems) {
      const listItem = window.document.createElement('li')
      listItem.appendChild(this.createResultElement(resultItem, searchString))
      this.dropDownList.appendChild(listItem)
    }

    this.selectedItemIndex = -1
    this.dropDownList.scrollTop = 0
  }

  /**
   * The default create item element displays the matched label and highlights the
   * matched text.
   */
  private createResultElement(
    resultItem: ResultItem,
    query: string
  ): HTMLDivElement {
    const container = document.createElement('div')
    container.className = `item${!resultItem.isVisible ? ' hidden' : ''}`

    const icon = this.createItemIcon(resultItem)
    container.appendChild(icon)

    const text = this.createTextContent(resultItem, query)
    container.appendChild(text)

    const focusBtn = this.createFocusBtn(resultItem)
    container.appendChild(focusBtn)

    container.addEventListener('click', () => {
      this.removeSelectedCssClass()
      this.selectItem(resultItem.item)
    })

    return container
  }

  private createTextContent(resultItem: ResultItem, query: string) {
    const textDiv = document.createElement('div')
    if (resultItem.key) {
      const keySpan = document.createElement('span')
      keySpan.className = 'key'
      keySpan.innerText = `${resultItem.key}: `
      textDiv.appendChild(keySpan)
    }

    // highlight the hit
    const value = resultItem.value
    const beginIndex = value.toLowerCase().indexOf(query)
    const endIndex = beginIndex + query.length
    textDiv.appendChild(document.createTextNode(value.substr(0, beginIndex)))
    const highlightSpan = document.createElement('span')
    highlightSpan.setAttribute('class', 'highlighted')
    highlightSpan.appendChild(
      document.createTextNode(value.substr(beginIndex, endIndex - beginIndex))
    )
    textDiv.appendChild(highlightSpan)
    textDiv.appendChild(
      document.createTextNode(value.substr(endIndex, value.length))
    )
    textDiv.title = !resultItem.isVisible
      ? 'Item is currently filtered out of the graph'
      : value
    return textDiv
  }

  /**
   * Helper method to select the given item in the graph.
   */
  private selectItem(item: IModelItem): void {
    this.graphComponent.selection.clear()
    this.graphComponent.selection.setSelected(item, true)
  }

  private searchGraph(query: string): ResultItem[] {
    if (query.length === 0) {
      return []
    }

    const hits: ResultItem[] = []

    const viewGraph = this.graphComponent.graph

    const searchableItems = this.graph.nodes.concat(
      this.graph.edges
    ) as IEnumerable<INode | IEdge>

    for (const item of searchableItems) {
      // match the label(s)
      for (const label of item.labels) {
        if (label.text.toLowerCase().indexOf(query) >= 0) {
          hits.push({
            item: item,
            value: label.text,
            type:
              item instanceof INode ? ResultItemType.NODE : ResultItemType.EDGE,
            isVisible: viewGraph.contains(item),
          })
        }
      }

      // match properties record
      const tag = item.tag
      if (tag.properties) {
        for (const key of Object.keys(tag.properties)) {
          const value = tag.properties[key]
          if (
            typeof value === 'string' &&
            value.toLocaleLowerCase().indexOf(query) >= 0
          ) {
            hits.push({
              item: item,
              key,
              value,
              type:
                item instanceof INode
                  ? ResultItemType.NODE
                  : ResultItemType.EDGE,
              isVisible: viewGraph.contains(item),
            })
          } else if (typeof value === 'number' && `${value}` === query) {
            hits.push({
              item: item,
              key,
              value: `${value}`,
              type:
                item instanceof INode
                  ? ResultItemType.NODE
                  : ResultItemType.EDGE,
              isVisible: viewGraph.contains(item),
            })
          } else if (Array.isArray(value)) {
            const hit = value
              .filter((v) => typeof v === 'string')
              .find((str) => str.toLowerCase().indexOf(query) >= 0)
            if (hit) {
              hits.push({
                item: item,
                key,
                value: hit,
                type:
                  item instanceof INode
                    ? ResultItemType.NODE
                    : ResultItemType.EDGE,
                isVisible: viewGraph.contains(item),
              })
            }
          }
        }
      }
    }

    return hits
  }

  private createFocusBtn(resultItem: ResultItem) {
    const btn = document.createElement('button')
    btn.onclick = (e) => {
      e.stopPropagation()
      const item = resultItem.item
      this.selectItem(item)
      if (LeafletSupport.isInMapMode(this.widgetRootElement)) {
        btn.dispatchEvent(
          new CustomEvent('yjg-zoom-to-item', { bubbles: true, detail: item })
        )
      } else {
        if (resultItem.type === ResultItemType.NODE) {
          const node = item as INode
          this.graphComponent.zoomToAnimated(
            node.layout.toRect().getEnlarged(100)
          )
        } else {
          const edge = item as IEdge
          const targetBounds = Rect.add(
            edge.sourceNode!.layout.toRect(),
            edge.targetNode!.layout.toRect()
          ).getEnlarged(100)
          this.graphComponent.zoomToAnimated(targetBounds)
        }
      }
    }
    btn.className = 'button focus'
    btn.title = 'Show in graph'

    const icon = createIconSvg(this.widgetRootElement, mdiEye, '#666')
    btn.appendChild(icon)

    return btn
  }

  private createItemIcon(resultItem: ResultItem): HTMLSpanElement {
    let icon: HTMLSpanElement
    if (resultItem.type === ResultItemType.NODE) {
      icon = createMdiIconSpan(
        this.widgetRootElement,
        mdiCheckboxBlankCircle,
        nodeFill,
        'Node'
      )
    } else {
      icon = createMdiIconSpan(
        this.widgetRootElement,
        mdiRayStartArrow,
        edgeStroke,
        'Edge'
      )
    }
    return icon
  }
}
