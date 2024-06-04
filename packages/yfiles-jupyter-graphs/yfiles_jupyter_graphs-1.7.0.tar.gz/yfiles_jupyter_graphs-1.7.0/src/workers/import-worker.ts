function createWorker(): any {
  // @ts-ignore
  return new Worker(new URL('./layout.worker.js', import.meta.url))
}

export default createWorker
