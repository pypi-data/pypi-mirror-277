/**
 * NOTE: This files needs to be JS.
 * ================================
 *
 * The Jupyterlab build parses the import tree of the project in the /lib/
 * folder (which contains the transpiled JS files) and thus wouldn't find the
 * './layout.worker.ts' file of the Worker import.
 *
 * IMPORTANT:
 * ==========
 *
 * The yfiles imports here must be module splitted because they are loaded in the worker as well.
 *
 * This is necessary for the jupyter labextension bundle to work correctly. For whatever reason, loading from yfiles
 * does NOT work in the labextension bundle. The 'jupyter labextension build' internally uses Webpack 5 with Module
 * Federation. Maybe it is misconfigured somehow or there is a problem regarding Module Federation with this approach.
 */
import { LayoutExecutorAsyncWorker } from 'yfiles/view-layout-bridge'
import { License } from 'yfiles/lang'
import license from '../yfiles-license.json'
import { LAYOUT_ALGORITHMS } from '../algorithm'

License.value = license

/**
 * @yjs:keep=properties
 */
function applyLayout(graph, layoutDescriptor) {
  const layoutKey = layoutDescriptor.properties.layoutKey
  const layout = LAYOUT_ALGORITHMS[layoutKey].layout
  layout.applyLayout(graph)
}

// eslint-disable-next-line no-undef
addEventListener(
  'message',
  (e) => {
    const currentTransaction = e.data.transaction
    const executor = new LayoutExecutorAsyncWorker(applyLayout)
    executor
      .process(e.data)
      .then((e) => {
        e.transaction = currentTransaction
        // eslint-disable-next-line no-undef
        postMessage(e)
      })
      .catch((e) => {
        e.transaction = currentTransaction
        // eslint-disable-next-line no-undef
        postMessage(e)
      })
  },
  false
)

// signal that the web worker thread is ready to execute
// eslint-disable-next-line no-undef
postMessage('ready')
