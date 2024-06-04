import {
  DefaultLabelStyle,
  EdgeStyleDecorationInstaller,
  ExteriorLabelModel,
  Fill,
  FreeNodeLabelModel,
  GroupNodeStyle,
  GroupNodeStyleTabPosition,
  IArrow,
  IEdge,
  ILabel,
  ILabelModelParameter,
  ILabelStyle,
  INode,
  INodeStyle,
  Insets,
  LabelShape,
  LabelStyleDecorationInstaller,
  PolylineEdgeStyle,
  Rect,
  ShapeNodeShape,
  ShapeNodeStyle,
  Size,
  Stroke,
  StyleDecorationZoomPolicy,
} from 'yfiles'
import { Edge, Node as Node_ } from './typings'
import { tinycolor } from '@ctrl/tinycolor'
import { isDarkMode } from './theme-support'

type ParsedStyles = {
  shape:
    | 'ellipse'
    | 'hexagon'
    | 'hexagon2'
    | 'octagon'
    | 'pill'
    | 'rectangle'
    | 'round-rectangle'
    | 'triangle'
  fill: string
  stroke: string
  image?: string
}

export const nodeBaseSize = [55.0, 55.0]
export const edgeBaseStroke = 2

//export const yfilesPrimaryColor = '#242265'
export const yfilesSecondaryColor = '#ff6c00'
export const nodeShape = 'ellipse'
export const nodeFill = '#15AFAC'
export const nodeStroke = '#15AFAC'
export const edgeStroke = '#15AFAC'
export const nodeLabelBackgroundFill = 'rgba(255, 255, 255, 0.7)'
export const edgeLabelBackgroundFill = 'rgba(255, 255, 255)'
export const textFill = '#0942c4b'

export const svgNodeStyle = new ShapeNodeStyle({
  shape: nodeShape,
  fill: nodeFill,
  stroke: nodeStroke,
})

export const svgEdgeStyleDirected = new PolylineEdgeStyle({
  stroke: `2px ${edgeStroke}`,
  targetArrow: `${edgeStroke} small triangle`,
  smoothingLength: 30,
})

export const svgEdgeStyleUndirected = new PolylineEdgeStyle({
  stroke: `2px ${edgeStroke}`,
  smoothingLength: 30,
})

export const DEFAULT_TAB_WIDTH = 30
export const DEFAULT_TAB_HEIGHT = 20

function getNodeSize(data: Node_): number[] {
  let size = nodeBaseSize
  if (typeof data.size !== 'undefined') {
    size = data.size
  }
  if (typeof data.scale_factor !== 'undefined') {
    return [size[0] * data.scale_factor, size[1] * data.scale_factor]
  } else {
    return size
  }
}

function getPosition(data: Node_): number[] {
  return typeof data.position === 'undefined' ? [0.0, 0.0] : data.position
}

export function getNodeLayoutProvider(): (d: Node_) => Rect {
  return (data) => {
    const [width, height] = getNodeSize(data)
    const [x, y] = getPosition(data)
    return new Rect(x, y, width, height)
  }
}

export function parseNodeLabelObjectParameter(tag: any): ILabelModelParameter {
  const styles = tag.styles?.label_styles ?? {}
  const position = styles.position as string | undefined
  if (position) {
    switch (position.toLowerCase()) {
      case 'north':
        return ExteriorLabelModel.NORTH
      case 'east':
        return ExteriorLabelModel.EAST
      case 'south':
        return ExteriorLabelModel.SOUTH
      case 'west':
        return ExteriorLabelModel.WEST
      case 'center':
        return FreeNodeLabelModel.INSTANCE.createDefaultParameter()
    }
  }
  return FreeNodeLabelModel.INSTANCE.createDefaultParameter()
}

//@yjs:keep=textAlignment
export function parseLabelObject(tag: any, isEdgeLabel = false): ILabelStyle {
  let styles: Record<string, any> = {}
  if (isEdgeLabel) {
    styles = tag.label_styles ?? {}
  } else {
    styles = tag.styles?.label_styles ?? {}
  }

  if (Object.keys(styles).length === 0) {
    const defaultStyle = new DefaultLabelStyle({
      backgroundFill: isEdgeLabel
        ? edgeLabelBackgroundFill
        : nodeLabelBackgroundFill,
      textFill,
      insets: [2, 4],
      shape: LabelShape.ROUND_RECTANGLE,
    })
    if (isEdgeLabel) {
      defaultStyle.backgroundStroke = new Stroke(getEdgeStroke(tag), 2)
    }
    return defaultStyle
  }

  let backgroundFill = isEdgeLabel
    ? edgeLabelBackgroundFill
    : nodeLabelBackgroundFill
  if (isDefined(styles.backgroundColor)) {
    backgroundFill = styles.backgroundColor
  }
  let textSize = 12
  if (isDefined(styles.fontSize)) {
    textSize = styles.fontSize
  }
  let textColor: string = textFill
  if (isDefined(styles.color)) {
    textColor = styles.color
  }
  const userStyle = new DefaultLabelStyle({
    backgroundFill: backgroundFill,
    textFill: textColor,
    textSize: textSize,
    insets: [2, 4],
    shape: LabelShape.ROUND_RECTANGLE,
  })
  if (isDefined(styles.maximumWidth) || isDefined(styles.maximumHeight)) {
    userStyle.maximumSize = new Size(
      styles.maximumWidth ?? Number.POSITIVE_INFINITY,
      styles.maximumHeight ?? Number.POSITIVE_INFINITY
    )
  }
  if (isDefined(styles.wrapping)) {
    userStyle.wrapping = styles.wrapping
  }
  if (isDefined(styles.textAlignment)) {
    userStyle.horizontalTextAlignment = styles.textAlignment
  }
  if (isEdgeLabel) {
    userStyle.backgroundStroke = new Stroke(getEdgeStroke(tag), 2)
  }
  return userStyle
}

export function parseStyleObject(tag: any): ParsedStyles {
  const styles = tag.styles ?? {}

  // color may be null to make it non-filled
  let fill = nodeFill
  if (isDefined(styles.color)) {
    fill = styles.color
  } else if (isDefined(tag.color)) {
    fill = tag.color
  }

  // make sure to have a stroke if fill is null
  const stroke = fill
    ? tinycolor(fill).darken(30).toString('hex6')
    : tinycolor(nodeFill).darken(30).toString('hex6')

  return {
    shape: styles.shape ?? nodeShape,
    fill,
    stroke,
    image: styles.image,
  }
}

export function getGroupStyling(node: INode): GroupNodeStyle {
  let fill: Fill | null = Fill.from(nodeFill)
  let stroke: Stroke | null = Stroke.from(nodeStroke)
  if (node.style instanceof ShapeNodeStyle) {
    fill = node.style.fill
    stroke = node.style.stroke
  }

  const gns = new GroupNodeStyle({
    tabPosition: GroupNodeStyleTabPosition.TOP_TRAILING,
    tabFill: fill,
    stroke: stroke,
    contentAreaFill: isDarkMode() ? '#1e1e1e' : '#fff',
  })

  // consider the first label as tab label
  const { width, height } = getTabSize(node, gns)
  gns.tabWidth = width
  gns.tabHeight = height

  return gns
}

export function getTabSize(node: INode, groupNodeStyle: GroupNodeStyle): Size {
  // consider the first label as tab label
  const label = node.labels.at(0)
  if (!label) {
    return new Size(groupNodeStyle.tabWidth, groupNodeStyle.tabHeight)
  }

  const { tabInset } = groupNodeStyle
  const width =
    label.preferredSize.width +
    (label.style as DefaultLabelStyle).insets.horizontalInsets +
    2 * tabInset
  const height = Math.max(
    label.preferredSize.height + tabInset,
    DEFAULT_TAB_HEIGHT
  )
  return new Size(width, height)
}

//@yjs:keep=directed
export function getEdgeDirection(directed: boolean, edgeData: Edge): boolean {
  const _directed = edgeData.directed
  return typeof _directed === 'undefined' ? directed : _directed
}

export function getEdgeStroke(edgeData: Edge): string {
  return typeof edgeData.color === 'undefined' ? edgeStroke : edgeData.color
}

export function getEdgeStrokeThickness(edgeData: Edge): number {
  return typeof edgeData.thickness_factor === 'undefined'
    ? edgeBaseStroke
    : edgeData.thickness_factor * edgeBaseStroke
}

const selectionStroke = new Stroke(yfilesSecondaryColor, 3)
selectionStroke.freeze()

export function getSelectionNodeStyle(node: INode): INodeStyle {
  let shape = ShapeNodeShape.ROUND_RECTANGLE
  if (node.style instanceof ShapeNodeStyle) {
    shape = node.style.shape
  }
  return new ShapeNodeStyle({
    shape,
    stroke: selectionStroke,
    fill: 'transparent',
  })
}

function selectionEdgeStyleProvider(
  directed: boolean,
  edgeData: Edge
): PolylineEdgeStyle {
  return new PolylineEdgeStyle({
    stroke: selectionStroke,
    targetArrow: getEdgeDirection(directed, edgeData)
      ? `${yfilesSecondaryColor} small triangle`
      : IArrow.NONE,
    smoothingLength: 30,
  })
}

export function getSelectionEdgeStyleProvider(
  directed: boolean
): (e: IEdge) => EdgeStyleDecorationInstaller {
  return (edge) => {
    return new EdgeStyleDecorationInstaller({
      edgeStyle: selectionEdgeStyleProvider(directed, edge.tag as Edge),
      zoomPolicy: StyleDecorationZoomPolicy.MIXED,
    })
  }
}

function getHighlightLabelStyle(
  labelStyle: DefaultLabelStyle
): DefaultLabelStyle {
  return new DefaultLabelStyle({
    backgroundStroke: new Stroke(
      yfilesSecondaryColor,
      labelStyle.backgroundStroke?.thickness ?? 2
    ),
    insets: labelStyle.insets,
    textFill: labelStyle.textFill,
    textSize: labelStyle.textSize,
    backgroundFill: labelStyle.backgroundFill,
    wrapping: labelStyle.wrapping,
    horizontalTextAlignment: labelStyle.horizontalTextAlignment,
    verticalTextAlignment: labelStyle.verticalTextAlignment,
    maximumSize: labelStyle.maximumSize,
    shape: labelStyle.shape,
  })
}

export function getSelectionEdgeLabelStyleProvider(): (
  e: ILabel
) => LabelStyleDecorationInstaller {
  return (e) => {
    return new LabelStyleDecorationInstaller({
      zoomPolicy: StyleDecorationZoomPolicy.WORLD_COORDINATES,
      labelStyle: getHighlightLabelStyle(e.style as DefaultLabelStyle),
      margins: new Insets(0),
    })
  }
}

function isDefined(value: unknown): boolean {
  return typeof value !== 'undefined'
}
