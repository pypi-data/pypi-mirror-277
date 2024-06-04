import {
  DefaultGraph,
  GraphComponent,
  GraphCopier,
  GraphMLIOHandler,
} from 'yfiles'

export function createConfiguredGraphMLIOHandler(): GraphMLIOHandler {
  return new GraphMLIOHandler()
}

export function exportGraphML(graphComponent: GraphComponent): Promise<string> {
  const targetGraph = new DefaultGraph()
  const copier = new GraphCopier()
  copier.copy({
    sourceGraph: graphComponent.graph,
    filter: () => true,
    targetGraph,
    elementCopiedCallback: (original, copy) => {
      copy.tag = consolidateDataObject(original.tag)
    },
  })

  targetGraph.tag = graphComponent.graph.tag

  const ioHandler = createConfiguredGraphMLIOHandler()
  return ioHandler.write(targetGraph)
}

/**
 * Creates a copy of the data object where duplicate information is consolidated in properties / styles.
 */
export function consolidateDataObject(original: any): any {
  if (!original) {
    return null
  }

  // we'll change the tag, so use a copy
  const copy = { ...original }
  if (typeof copy.color !== 'undefined') {
    // Consolidate the top-level color property in the styles object of the tag.
    // Note, the optional styles object overwrites any given top-level color property on the tag.
    copy.styles = Object.assign({ color: copy.color }, copy.styles)
    delete copy.color
  }

  return copy
}
