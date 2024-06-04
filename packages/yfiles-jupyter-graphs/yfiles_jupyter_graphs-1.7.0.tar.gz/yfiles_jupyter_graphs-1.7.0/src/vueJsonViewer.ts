import Vue from 'vue'
// @ts-ignore
import JsonViewer from 'vue-json-viewer'
import { INode, IEdge, IEnumerable } from 'yfiles'
import { edgeStroke, nodeBaseSize, nodeFill } from './graph-style-configuration'

Vue.use(JsonViewer)

/**
 * @yjs:keep=template
 */
const vueJsonViewerComponent = Vue.component('vueJsonViewer', {
  template: `
    <json-viewer copyable :value="jsonData">
    <template v-slot:copy>
      <div title="Copy json to clipboard" class="jv-copy-button"></div>
    </template>
    </json-viewer>`,
  data() {
    return {
      jsonData: {},
    }
  },
})

export class VueJsonViewer {
  private jvCache: Record<
    string,
    { vue: InstanceType<typeof vueJsonViewerComponent>; used: boolean }
  > = {}

  private getIdFromItem(item: INode | IEdge) {
    return (item instanceof INode ? 'node' : 'edge') + item.tag.id
  }

  /**
   * Creates the data blob that is displayed in the data-viewer panel of the widget.
   * For example, hide internal state that is in the tag which is not useful to the user, and also make the actual
   * business data top-level.
   *
   * @yjs:keep=properties
   */
  private createJsonViewData(item: IEdge | INode): Record<string, unknown> {
    const data = item.tag

    // gather internal state in this nested object
    const itemState = {} as Record<string, unknown>

    // don't show internal state on the viewer object
    // anything else is moved to a nested '_itemState' field
    const internalStateProperties = [
      'id',
      'start',
      'end',
      'positions',
      'color', // handled explicitly below
      'properties', // handled explicitly below
      'label_styles', //handled explicitly below
    ]

    for (const key of Object.keys(data)) {
      if (internalStateProperties.indexOf(key) === -1 && data[key]) {
        const value = data[key]
        // skip some default values
        if (key === 'scale_factor' && value === 1) {
          continue
        }
        if (key === 'thickness_factor' && value === 1) {
          continue
        }
        if (
          key === 'size' &&
          value[0] === nodeBaseSize[0] &&
          value[1] === nodeBaseSize[1]
        ) {
          continue
        }
        if (key === 'position' && value[0] === 0 && value[1] === 0) {
          continue
        }
        itemState[key] = value
      }
    }

    // the 'color' property should only be considered in the itemState, if it's not the default color
    const defaultColor = item instanceof INode ? nodeFill : edgeStroke
    if (data.color && data.color !== defaultColor) {
      if (!itemState.styles) {
        // there are no styles at all, so just add it
        itemState.styles = { color: data.color }
      } else {
        // there is already a style, so the color specified in it would overwrite the top-level color
        const styles = itemState.styles as Record<string, unknown>
        styles.color = styles.color ?? data.color
      }
    }
    if (data.label_styles && itemState.styles) {
      //edges have a styled label and other styling
      const styles = itemState.styles as Record<string, unknown>
      styles.label_styles = data.label_styles
    } else if (data.label_styles) {
      //edges have a styled label and no other styling
      itemState.styles = { label_styles: data.label_styles }
    }

    // styles may be empty
    const viewerStyles = itemState.styles as Record<string, unknown> | undefined
    if (viewerStyles && Object.keys(viewerStyles).length === 0) {
      delete itemState.styles
    }

    const viewerData = { ...data.properties }
    // item state may be empty
    if (Object.keys(itemState).length > 0) {
      viewerData['__itemState'] = itemState
    }
    return viewerData
  }

  /**
   * This tries to retrieve the vue component which is associated to the item. If the item is not cached we try
   * to get a vue component which is no longer in use but belonged to the same type (node, edge). If there is no
   * vue component to reuse, we create a new one and add it to the cache.
   * @param item
   */
  private getFromCache(
    item: INode | IEdge
  ): InstanceType<typeof vueJsonViewerComponent> {
    const id = this.getIdFromItem(item)
    let comp = this.jvCache[id]?.vue

    if (comp) {
      return comp
    }

    // element was not cached, try reuse a component with same type
    for (const [i, el] of Object.entries(this.jvCache)) {
      if (!el.used && i.startsWith(item instanceof INode ? 'node' : 'edge')) {
        comp = el.vue
        this.jvCache[id] = { vue: comp, used: true }
        return comp
      }
    }

    // try to use any vue component which is not used
    for (const el of Object.values(this.jvCache)) {
      if (!el.used) {
        comp = el.vue
        this.jvCache[id] = { vue: comp, used: true }
        return comp
      }
    }

    // could not reuse any component, create a new one
    const vueJsonViewer = new vueJsonViewerComponent()
    vueJsonViewer.$mount()
    this.jvCache[id] = { vue: vueJsonViewer, used: true }
    comp = vueJsonViewer

    return comp
  }

  private removeUnusedCacheItems(): void {
    const filteredCache: Record<
      string,
      { vue: InstanceType<typeof vueJsonViewerComponent>; used: boolean }
    > = {}
    for (const [id, el] of Object.entries(this.jvCache)) {
      if (el.used) {
        filteredCache[id] = el
      }
    }

    this.jvCache = filteredCache
  }

  private createDataEntry(item: INode | IEdge): HTMLDivElement {
    const json = this.createJsonViewData(item)
    let entry = document.createElement('div')
    entry.className = `data-entry ${item instanceof INode ? 'node' : 'edge'}`

    try {
      const jsonViewerElement = document.createElement('div')

      if (Object.keys(json).length > 0) {
        const vueComponent = this.getFromCache(item)
        vueComponent.jsonData = json
        jsonViewerElement.appendChild(vueComponent.$el)

        entry.appendChild(jsonViewerElement)
      } else {
        entry = document.createElement('div')
        entry.className = 'data-entry empty'
        entry.innerText = 'No data available'
      }
    } catch (e) {
      console.log(e)
      entry = document.createElement('div')
      entry.className = 'data-entry error'
      entry.innerText = 'Cannot display the given data item'
    }

    return entry
  }

  public addItems(
    dataPanel: HTMLDivElement,
    items: IEnumerable<INode | IEdge>
  ): void {
    // mark cached vue components which are reused
    const ids = items.map((i) => this.getIdFromItem(i))

    for (const [id, el] of Object.entries(this.jvCache)) {
      el.used = ids.includes(id)
    }

    for (const item of items) {
      const entry = this.createDataEntry(item)
      dataPanel.appendChild(entry)
    }

    this.removeUnusedCacheItems()
  }
}
