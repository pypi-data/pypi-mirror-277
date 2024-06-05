declare module './sampledata.json' {
  const value: Data
  export default value
}

export type ResultRecord = Node | Edge

type Id = number | string

export interface Node {
  id: Id
  parentId?: Id | null
  label: string
  color: string
  scale_factor: number
  type: Id | boolean
  properties: Properties
  size: number[]
  position: number[]
}

export interface Edge {
  id: Id
  start: Id
  end: Id
  label: string
  color: string
  thickness_factor: number
  directed: boolean
  properties: Properties
}

type Properties = Record<string, any>

export type LayoutConfig = {
  algorithm: string
  options: {}
}

export type ContextPaneConfig = {
  id: string
  title: string
}

export type HighlightEntry = { id: Id; value: any }

export type HighlightData = {
  nodes: HighlightEntry[]
  edges: HighlightEntry[]
}

export type Highlights = HighlightData[]

export type NeighborhoodConfig = {
  max_distance: number
  selected_nodes: unknown[]
}

export type SidebarConfig = {
  enabled: boolean
  start_with: string
}

export type OverviewConfig = {
  enabled: boolean
  overview_set: boolean
}

export type LicenseJson = {
  version: string
  domains: string[]
  expiry: string
}
export type SignedLicenseJson = LicenseJson & { signature: string }
