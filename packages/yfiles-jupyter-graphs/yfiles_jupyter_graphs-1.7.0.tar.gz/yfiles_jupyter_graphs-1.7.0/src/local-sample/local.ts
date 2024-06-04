import { GraphView } from '../widget'
import { WidgetModel } from '@jupyter-widgets/base'
import { Highlights } from '../typings'
import localSmallSample from './local-small-sample'
import localBigSample from './local-big-sample'
import { loadFlightDataSample } from './local-flight-data-sample'

/**
 * This file mocks the python sided input for the local playground (e.g. local:watch)
 */

const a = new GraphView({
  model: new WidgetModel({}, {}),
  el: document.getElementById('graph-component') as HTMLElement,
})

a.model.set('_overview', {
  // enabled: false,
})

a.model.set('_context_pane_mapping', [
  { id: 'Neighborhood', title: 'Neighborhood' },
  { id: 'Data', title: 'Data' },
  { id: 'Search', title: 'Search' },
  { id: 'About', title: 'About' },
])

a.model.set('_sidebar', {
  enabled: true,
  start_with: '',
})

a.model.set('_neighborhood', {
  max_distance: 2,
  selected_nodes: [2, 3],
})

a.model.set('_highlight', [
  {
    nodes: [
      /*
      { id: 0, value: 3.0 },
      { id: 1, value: 1.0 },*/
    ],
    edges: [
      /*{ id: 0, value: 7 }*/
    ],
    // highlighting: {
    //   TODO: maybe make highlighting customizable
    //   TODO: highlighting does not take edge direction into account
    //   node: { mappingType: 'linear', mappingTarget: 'fill' },
    //   edges: { mappingType: 'value', mappingTarget: 'size' },
    // },
  },
  {
    nodes: [
      /*{ id: 2, value: 1.0 }*/
    ],
    edges: [],
  },
] as Highlights)

a.model.set('_graph_layout', {
  algorithm: 'organic',
  options: {},
})

a.model.set('_directed', true)

// a.model.set('_nodes', localSmallSample.nodes)
// a.model.set('_edges', localSmallSample.edges)

// a.model.set('_nodes', localBigSample.nodes)
// a.model.set('_edges', localBigSample.edges)

loadFlightDataSample(a.model, true)

a.render()
