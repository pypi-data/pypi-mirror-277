import { Application, IPlugin } from '@lumino/application';

import { Widget } from '@lumino/widgets';

import { IJupyterWidgetRegistry } from '@jupyter-widgets/base'

import * as widgetExports from './widget'

import { MODULE_NAME, MODULE_VERSION } from './version'

const EXTENSION_ID = 'yfiles-jupyter-graphs:plugin'

/**
 * The graph plugin.
 */
const graphPlugin: IPlugin<Application<Widget>, void> = {
  id: EXTENSION_ID,
  requires: [IJupyterWidgetRegistry],
  activate: activateWidgetExtension,
  autoStart: true,
} as unknown as IPlugin<Application<Widget>, void>
// the "as unknown as ..." typecast above is solely to support JupyterLab 1
// and 2 in the same codebase and should be removed when we migrate to Lumino.

export default graphPlugin

let appEnvironment: Application<Widget> | null = null
export function getAppEnvironment(): Application<Widget> | null {
  // is initialized upon registration
  return appEnvironment
}

/**
 * Activate the widget extension.
 */
function activateWidgetExtension(
  app: Application<Widget>,
  registry: IJupyterWidgetRegistry
): void {
  appEnvironment = app
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: widgetExports,
  })
}
