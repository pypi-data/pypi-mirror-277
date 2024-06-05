import { MouseHoverInputMode, Point } from 'yfiles'

/**
 * Adjusts the tooltip position such that it stays within the widget's cell, otherwise
 * tooltip content would be clipped by the given cell of JupyterLab / Notebook.
 */
export class AdjustingMouseHoverInputMode extends MouseHoverInputMode {
  /**
   * NOTE: Overwritten onShow because adjustToolTipLocation didn't do the trick here...
   */
  protected onShow(location: Point, content?: any): Promise<boolean> {
    return super.onShow(location, content).then((visible) => {
      const root = this.toolTipParentElement
      if (visible && this.toolTip && root) {
        const rootBounds = root.getBoundingClientRect()

        const cc = this.inputModeContext!.canvasComponent!
        const tooltipLocation = cc.toPageFromView(
          cc.toViewCoordinates(location)
        )

        // the tooltip is positioned relative to the root container, so (0,0) is top-left of the cell
        const pageLocationX =
          tooltipLocation.x + this.toolTipLocationOffset.x - rootBounds.left
        const pageLocationY =
          tooltipLocation.y + this.toolTipLocationOffset.y - rootBounds.top

        // the cell may be clipped by the page's viewport, so maybe limit the available space
        // unfortunately, jupyterlab doesn't scroll the body but some element within it, so this may fail and clip
        // the tooltip at the bottom of the page
        const documentElement = document.documentElement
        const availableWidth =
          rootBounds.width -
          Math.max(
            0,
            rootBounds.left + rootBounds.width - documentElement.clientWidth
          )
        const availableHeight =
          rootBounds.height -
          Math.max(
            0,
            rootBounds.top + rootBounds.height - documentElement.clientHeight
          )

        // move tooltip into the cell
        const maxX = availableWidth - this.toolTip.desiredSize.width
        const maxY = availableHeight - this.toolTip.desiredSize.height
        const left = Math.max(0, Math.min(pageLocationX, maxX))
        const top = Math.max(0, Math.min(pageLocationY, maxY))

        this.toolTip.div.style.left = `${left}px`
        this.toolTip.div.style.top = `${top}px`
      }
      return visible
    })
  }
}
