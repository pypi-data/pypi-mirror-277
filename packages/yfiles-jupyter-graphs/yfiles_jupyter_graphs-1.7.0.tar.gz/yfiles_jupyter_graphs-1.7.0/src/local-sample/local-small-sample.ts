const nodes = [
  {
    id: 0,
    label: 'Person',
    properties: {
      firstName: 'Ali',
    },
    scale_factor: 2,
    positions: [0.0, 0.0],
  },
  {
    id: 1,
    label: 'Person',
    properties: {
      firstName: 'Bernd',
    },
    positions: [0.0, 0.0],
  },
  {
    id: 2,
    label: 'Person',
    properties: {
      firstName: 'Clara',
    },
    scale_factor: 0.5,
    positions: [0.0, 0.0],
  },
  {
    id: 3,
    label: 'Person',
    properties: {
      firstName: 'Don',
    },
    positions: [0.0, 0.0],
  },
  {
    id: 4,
    label: '',
    properties: {
      firstName: 'Emile',
    },
    scale_factor: 1.0,
    positions: [0.0, 0.0],
  },
]

/**
 * @yjs:keep=start,end
 */
const edges = [
  {
    id: 0,
    start: 0,
    end: 1,
    label: 'knows',
    properties: {
      since: 1992,
    },
    directed: false,
  },
  {
    id: 1,
    start: 1,
    end: 2,
    label: 'knows',
    properties: {
      since: 2007,
    },
    thickness_factor: 2,
  },
  {
    id: 2,
    start: 2,
    end: 3,
    label: 'knows',
    properties: {
      since: 2001,
    },
    directed: false,
  },
  {
    id: 3,
    start: 3,
    end: 1,
    label: 'knows',
    properties: {
      since: 2017,
    },
    thickness_factor: 0.5,
  },
  {
    id: 4,
    start: 1,
    end: 4,
    label: '',
    properties: {
      since: 1992,
      location: {
        city: 'Berlin',
        country: 'Germany',
      },
    },
    directed: false,
  },
]

export default {
  nodes,
  edges,
}
