import { getAppEnvironment } from './plugin'

const DARK_THEME_CSS_CLASS = 'dark-mode'

/**
 * Get the JupyterLab plugin registered with the given id.
 */
function getPlugin(pluginId: string): Record<string, any> | null {
  const env = getAppEnvironment()
  if (!env || !env.hasPlugin(pluginId)) {
    return null
  }
  // there is no official API to get the actual plugin, and there seem to be different implementations, so we
  // do our best, see also
  // https://github.com/jupyterlab/jupyterlab/blob/9ad40ceed4f74470f2ea1d99f12c883f8d460a16/galata/src/inpage/index.ts#L50-L66
  // @ts-expect-error: _plugins is the list of registered plugins when running JupyterLab environment
  return env._plugins?.get(pluginId) ?? env._pluginMap[pluginId] ?? null
}

//@yjs:keep=theme,service
function getCurrentJupyterLabTheme(): string | undefined {
  const themeProvider = getPlugin('@jupyterlab/apputils-extension:themes')
  return themeProvider?.service?.theme
}

export function isDarkMode(): boolean {
  const jupyterLabTheme = getCurrentJupyterLabTheme()
  if (jupyterLabTheme) {
    return jupyterLabTheme === 'JupyterLab Dark'
  }

  // try to detect google colab theme
  const colabEditorAttr = document.documentElement.getAttribute('editor')
  if (colabEditorAttr) {
    return colabEditorAttr.toLowerCase().indexOf('dark') !== -1
  }

  return window.matchMedia('(prefers-color-scheme: dark)').matches
}

export function updateThemeClass(widgetRootElement: HTMLElement): void {
  if (isDarkMode()) {
    widgetRootElement.classList.add(DARK_THEME_CSS_CLASS)
  } else {
    widgetRootElement.classList.remove(DARK_THEME_CSS_CLASS)
  }
}
