// @ts-ignore
import Worker from './layout.worker.js'

/**
 * Inlines this worker when loading with worker-loader. Can be used alternatively to the default worker bundling.
 *
 * Note: This is necessary for the CDN bundle to support the worker.
 */
function createWorker(): any {
  return new Worker()
}

export default createWorker
