import {
  Animator,
  CopiedLayoutGraph,
  FilteredGraphWrapper,
  GraphComponent,
  GraphConnectivity,
  GraphEditorInputMode,
  IInputMode,
  INode,
  InteractiveOrganicLayout,
  InteractiveOrganicLayoutExecutionContext,
  LayoutGraphAdapter,
  MoveInputMode,
  YNode,
} from 'yfiles'
import { showToast, straightenEdges } from './utils'

/**
 * The layout algorithm.
 */
let layout: InteractiveOrganicLayout | null = null
let animator: Animator | null = null
const MAX_TIME = 1000
/**
 * The copy of the graph used for the layout.
 */
let copiedLayoutGraph: CopiedLayoutGraph

/**
 * Holds the nodes that are moved during dragging.
 */
let movedNodes: INode[]

/**
 * The context that provides control over the layout calculation.
 */
let layoutContext: InteractiveOrganicLayoutExecutionContext

/**
 * The hidden nodes of the widget
 */
let hidden: Set<INode> | null = null

function toggleGroupNodes(
  graphComponent: GraphComponent,
  showGroupNodes: boolean
): void {
  const filteredGraphWrapper = graphComponent.graph as FilteredGraphWrapper
  const fullGraph = filteredGraphWrapper.wrappedGraph!
  let showHiddenNodesToast = false
  for (const node of fullGraph.nodes) {
    if (fullGraph.isGroupNode(node)) {
      if (showGroupNodes) {
        hidden?.delete(node)
      } else {
        hidden?.add(node)
        showHiddenNodesToast = true
      }
    }
  }
  filteredGraphWrapper.nodePredicateChanged()
  if (showHiddenNodesToast) {
    showToast(
      graphComponent.div.parentElement!,
      'Group nodes are hidden while using the interactive organic layout',
      undefined,
      true
    )
  }
}

export async function startInteractiveOrganicLayout(
  graphComponent: GraphComponent,
  hiddenNodes: Set<INode>
): Promise<void> {
  hidden = hiddenNodes

  straightenEdges(graphComponent)
  graphComponent.inputMode = changeEditorMode(graphComponent)

  // hide group nodes for interactive organic layout
  toggleGroupNodes(graphComponent, false)

  const graph = graphComponent.graph
  // create a copy of the graph for the layout algorithm
  copiedLayoutGraph = new LayoutGraphAdapter(graph).createCopiedLayoutGraph()

  // create and start the layout algorithm
  layout = startLayout(graphComponent)
  wakeUp(graphComponent)
}

export function stopInteractiveOrganicLayout(
  graphComponent: GraphComponent
): void {
  // stop layout
  layout?.stop()
  animator?.stop()
  layout = null
  animator = null

  // disable node movement
  const inputMode = graphComponent.inputMode as GraphEditorInputMode
  inputMode.moveUnselectedInputMode.enabled = false

  // de-register callbacks
  const moveUnselectedInputMode = inputMode.moveUnselectedInputMode
  moveUnselectedInputMode.removeDragStartedListener(onMoveInitialized)
  moveUnselectedInputMode.removeDragCanceledListener(onMoveCanceled)
  moveUnselectedInputMode.removeDraggedListener(onMoving)
  moveUnselectedInputMode.removeDragFinishedListener(onMovedFinished)

  // show group nodes again
  toggleGroupNodes(graphComponent, true)
  hidden = null
}
/**
 * Creates the input mode for the graphComponent.
 * @returns a new GraphEditorInputMode instance
 */
function changeEditorMode(graphComponent: GraphComponent): IInputMode {
  // create default interaction with a number of disabled input modes.
  const mode = graphComponent.inputMode! as GraphEditorInputMode

  // prepare the move input mode for interacting with the layout algorithm
  mode.moveUnselectedInputMode.enabled = true
  initMoveMode(mode.moveUnselectedInputMode)

  return mode
}

/**
 * Registers the listeners to the given move input mode in order to tell the organic layout what
 * nodes are moved interactively.
 * @param moveInputMode The input mode that should be observed
 */
function initMoveMode(moveInputMode: MoveInputMode): void {
  // register callbacks to notify the organic layout of changes
  moveInputMode.addDragStartedListener(onMoveInitialized)
  moveInputMode.addDragCanceledListener(onMoveCanceled)
  moveInputMode.addDraggedListener(onMoving)
  moveInputMode.addDragFinishedListener(onMovedFinished)
}

/**
 * Called once the move operation has been initialized.
 * Calculates which components stay fixed and which nodes will be moved by the user.
 * @param affectedItems The dragged items
 */
function onMoveInitialized({ affectedItems }: MoveInputMode): void {
  if (layout !== null) {
    const copy = copiedLayoutGraph
    const componentNumber = copy.createNodeMap()
    GraphConnectivity.connectedComponents(copy, componentNumber)
    const movedComponents = new Set()
    const selectedNodes = new Set()
    movedNodes = affectedItems.ofType(INode.$class).toArray()
    for (const node of movedNodes) {
      const copiedNode = copy.getCopiedNode(node)
      if (copiedNode !== null) {
        // remember that we nailed down this node
        selectedNodes.add(copiedNode)
        // remember that we are moving this component
        movedComponents.add(componentNumber.getInt(copiedNode))
        // Update the position of the node in the CLG to match the one in the IGraph
        layout.setCenter(
          copiedNode,
          node.layout.x + node.layout.width * 0.5,
          node.layout.y + node.layout.height * 0.5
        )
        // Actually, the node itself is fixed at the start of a drag gesture
        layout.setInertia(copiedNode, 1.0)
        // Increasing has the effect that the layout will consider this node as not completely placed...
        // In this case, the node itself is fixed, but it's neighbors will wake up
        increaseHeat(copiedNode, layout, 0.5)
      }
    }

    // make all nodes that are not actively moved float freely
    for (const copiedNode of copy.nodes) {
      if (!selectedNodes.has(copiedNode)) {
        layout.setInertia(copiedNode, 0)
      }
    }

    // dispose the map
    copy.disposeNodeMap(componentNumber)

    // Notify the layout that there is new work to do...
    layout.wakeUp()
  }
}

/**
 * Notifies the layout of the new positions of the interactively moved nodes.
 */
function onMoving(): void {
  if (layout !== null) {
    for (const node of movedNodes) {
      const copiedNode = copiedLayoutGraph.getCopiedNode(node)
      if (copiedNode !== null) {
        // Update the position of the node in the CLG to match the one in the IGraph
        layout.setCenter(copiedNode, node.layout.center.x, node.layout.center.y)
        // Increasing the heat has the effect that the layout will consider these nodes as not completely placed...
        increaseHeat(copiedNode, layout, 0.05)
      }
    }
    // Notify the layout that there is new work to do...
    layout.wakeUp()
  }
}

/**
 * Resets the state in the layout when the user cancels the move operation.
 */
function onMoveCanceled(): void {
  if (layout !== null) {
    const copy = copiedLayoutGraph
    for (const node of movedNodes) {
      const copiedNode = copy.getCopiedNode(node)
      if (copiedNode !== null) {
        // Update the position of the node in the CLG to match the one in the IGraph
        layout.setCenter(copiedNode, node.layout.center.x, node.layout.center.y)
        layout.setStress(copiedNode, 0)
      }
    }
    for (const copiedNode of copy.nodes) {
      // Reset the node's inertia to be fixed
      layout.setInertia(copiedNode, 1)
      layout.setStress(copiedNode, 0)
    } // We don't want to restart the layout (since we canceled the drag anyway...)
  }
}
/**
 * Called once the interactive move is finished.
 * Updates the state of the interactive layout.
 */
function onMovedFinished(): void {
  if (layout !== null) {
    const copy = copiedLayoutGraph
    for (const node of movedNodes) {
      const copiedNode = copy.getCopiedNode(node)
      if (copiedNode !== null) {
        // Update the position of the node in the CLG to match the one in the IGraph
        layout.setCenter(copiedNode, node.layout.center.x, node.layout.center.y)
        layout.setStress(copiedNode, 0)
      }
    }
    for (const copiedNode of copy.nodes) {
      // Reset the node's inertia to be fixed
      layout.setInertia(copiedNode, 1)
      layout.setStress(copiedNode, 0)
    }
  }
}

/**
 * Creates a new layout instance and starts a new execution context for it.
 */
function startLayout(graphComponent: GraphComponent): InteractiveOrganicLayout {
  // create the layout
  const organicLayout = new InteractiveOrganicLayout({
    maximumDuration: MAX_TIME,
    // The compactness property prevents component drifting.
    compactnessFactor: 0.6,
  })

  layoutContext = organicLayout.startLayout(copiedLayoutGraph)
  // use an animator that animates an infinite animation
  animator = new Animator(graphComponent)
  animator.autoInvalidation = false
  animator.allowUserInteraction = true

  void animator.animate(() => {
    layoutContext.continueLayout(20)
    if (organicLayout.commitPositionsSmoothly(50, 0.05) > 0) {
      graphComponent.updateVisual()
    }
  }, Number.POSITIVE_INFINITY)

  return organicLayout
}

/**
 * Wakes up the layout algorithm.
 */
function wakeUp(graphComponent: GraphComponent): void {
  if (layout !== null) {
    // we make all nodes freely movable
    for (const copiedNode of copiedLayoutGraph.nodes) {
      layout.setInertia(copiedNode, 0)
    }
    // then wake up the layout
    layout.wakeUp()

    const geim = graphComponent.inputMode as GraphEditorInputMode
    // and after two seconds we freeze the nodes again...
    window.setTimeout(() => {
      if (
        geim.moveInputMode.isDragging ||
        geim.moveUnselectedInputMode.isDragging
      ) {
        // don't freeze the nodes if a node is currently being moved
        return
      }
      for (const copiedNode of copiedLayoutGraph.nodes) {
        layout!.setInertia(copiedNode, 1)
      }
    }, 2000)
  }
}

/**
 * Helper method that increases the heat of the neighbors of a given node by a given value.
 * This will make the layout algorithm move the neighbor nodes more quickly.
 */
function increaseHeat(
  copiedNode: YNode,
  layoutAlgorithm: InteractiveOrganicLayout,
  delta: number
): void {
  // Increase Heat of neighbors
  for (const neighbor of copiedNode.neighbors) {
    const oldStress = layoutAlgorithm.getStress(neighbor)
    layoutAlgorithm.setStress(neighbor, Math.min(1, oldStress + delta))
  }
}
