import createWorker from './workers/import-worker'
import {
  CompositeLayoutData,
  GraphComponent,
  LayoutData,
  LayoutExecutorAsync,
  PortAdjustmentPolicy,
} from 'yfiles'
import { LayoutStyle } from './algorithm'

/**
 * Keep track of a 'main' worker to avoid warming up a fresh worker for each and every layout.
 * However, we still support secondary layout workers to support the page initialization, where
 * multiple widgets may be initialized in parallel.
 */
function createLayoutWorker(): Promise<Worker | null> {
  // noinspection JSUnusedLocalSymbols
  return new Promise((resolve, reject) => {
    if (LayoutSupport.mainWorker && !LayoutSupport.mainWorkerBusy) {
      LayoutSupport.mainWorkerBusy = true
      resolve(LayoutSupport.mainWorker)
      return
    }

    let worker: Worker
    try {
      worker = createWorker()

      if (!LayoutSupport.mainWorker) {
        LayoutSupport.mainWorkerBusy = true
        LayoutSupport.mainWorker = worker
      }
    } catch (e) {
      resolve(null)
      return
    }

    worker.onmessage = (e: any) => {
      if (e.data === 'ready') {
        resolve(worker)
      }
    }
  })
}

let transaction = 0
export class LayoutSupport {
  private executor: LayoutExecutorAsync | null = null
  private static $layoutSupport: LayoutSupport

  static mainWorkerBusy = false
  static mainWorker: Worker | null = null

  static get INSTANCE(): LayoutSupport {
    if (!LayoutSupport.$layoutSupport) {
      LayoutSupport.$layoutSupport = new LayoutSupport()
    }
    return LayoutSupport.$layoutSupport
  }

  cancelLayout(): Promise<void> {
    if (!this.executor) {
      return Promise.resolve()
    }
    return this.executor.cancel()
  }

  private static configureNodeTypeOrder(layoutData: LayoutData) {
    // handle special case for organic layout data, see algorithm file
    if (layoutData instanceof CompositeLayoutData) {
      // eslint-disable-next-line @typescript-eslint/no-extra-semi
      ;(layoutData as CompositeLayoutData).items.forEach((data) => {
        LayoutSupport.configureNodeTypeOrder(data)
      })
      return
    }

    // @ts-ignore
    if (!layoutData.nodeTypes) {
      return
    }

    // @ts-ignore
    layoutData.nodeTypes.delegate = (node: any) => {
      return typeof node.tag.type === 'undefined' ? null : node.tag.type
    }
  }

  /**
   * @yjs:keep=properties
   */
  async morphLayout(
    graphComponent: GraphComponent,
    layoutStyle: LayoutStyle
  ): Promise<void> {
    if (!layoutStyle.layout) {
      return
    }

    const layoutWorker = await createLayoutWorker()

    if (!layoutWorker) {
      console.warn('Web Worker not supported. Running layout on client thread.')
      await graphComponent.morphLayout(
        layoutStyle.layout,
        '1s',
        layoutStyle.layoutData
      )
      return
    }

    // helper function that performs the actual message passing to the web worker
    function webWorkerMessageHandler(data: any): Promise<any> {
      const currentTransaction = transaction
      transaction++
      data.transaction = currentTransaction
      return new Promise((resolve, reject) => {
        layoutWorker!.addEventListener('message', function onmessage(e: any) {
          if (layoutWorker === LayoutSupport.mainWorker) {
            LayoutSupport.mainWorkerBusy = false // free the main worker
          } else {
            layoutWorker!.terminate() // destroy secondary workers when done
          }
          if (e.data && e.data.transaction === currentTransaction) {
            layoutWorker!.removeEventListener('message', onmessage)
            if (e.data.name === 'AlgorithmAbortedError') {
              reject(e.data)
            } else {
              resolve(e.data)
            }
          }
        })

        layoutWorker!.postMessage(data)
      })
    }

    if (layoutStyle.layoutData) {
      LayoutSupport.configureNodeTypeOrder(layoutStyle.layoutData)
    }

    // create an asynchronous layout executor that calculates a layout on the worker
    this.executor = new LayoutExecutorAsync({
      messageHandler: webWorkerMessageHandler,
      graphComponent,
      layoutDescriptor: {
        name: 'UserDefined',
        properties: {
          layoutKey: layoutStyle.key,
        },
      },
      layoutData: layoutStyle.layoutData,
      duration: '1s',
      animateViewport: true,
      easedAnimation: true,
      portAdjustmentPolicy: PortAdjustmentPolicy.ALWAYS,
    })

    // run the Web Worker layout
    return this.executor!.start()
  }
}
