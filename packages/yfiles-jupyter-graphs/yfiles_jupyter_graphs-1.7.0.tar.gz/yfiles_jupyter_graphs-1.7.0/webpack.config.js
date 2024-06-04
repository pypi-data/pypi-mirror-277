const webpack = require('webpack')
const path = require('path')
const version = require('./package.json').version
const TerserPlugin = require('terser-webpack-plugin')
const OptimizerPlugin = require('@yworks/optimizer/webpack-plugin')
const LicensePlugin = require('webpack-license-plugin')
const { OptimizerBlacklist } = require('./optimizer-blacklist')

// Custom webpack rules
const rules = [
  {
    test: /\.worker\.js$/,
    use: {
      loader: 'worker-loader',
      options: {
        inline: 'no-fallback',
        esModule: false,
      },
    },
  },
  {
    test: /\.tsx?$/,
    use: 'ts-loader',
    exclude: /node_modules/,
  },
  { test: /\.css$/, use: ['style-loader', 'css-loader'] },
]

// Packages that shouldn't be bundled but loaded at runtime
const externals = ['@jupyter-widgets/base', 'module']

const resolve = {
  extensions: ['.tsx', '.ts', '.js'],
  alias: {
    vue$: 'vue/dist/vue.esm.js',
    './workers/import-worker': path.resolve(
      __dirname,
      'src/workers/import-worker-inline'
    ),
  },
}

const commonConfig = {
  plugins: [
    new webpack.DefinePlugin({
      __VERSION__: JSON.stringify(version),
    }),
    new LicensePlugin({
      outputFilename: 'third-party-licenses.json',
      excludedPackageTest: (packageName) =>
        packageName === 'yfiles' || packageName === 'yfiles-jupyter-graphs',
      unacceptableLicenseTest: (licenseIdentifier) => {
        return ['GPL', 'AGPL', 'LGPL', 'NGPL'].includes(licenseIdentifier)
      },
      includePackages: () => [
        path.resolve(__dirname, 'node_modules', '@jupyter-widgets', 'base'),
      ],
    }),
  ],
}

/**
 * Notebook extension
 *
 * This bundle only contains the part of the JavaScript that is run on load of
 * the notebook.
 */
const notebookBundle = {
  entry: { index: './src/extension.ts' },
  output: {
    path: path.resolve(__dirname, 'yfiles_jupyter_graphs', 'nbextension'),
    library: { type: 'amd' }, // It must be an amd module
    publicPath: '', // publicPath is set in extension.js
  },
  module: {
    rules: rules,
  },
  devtool: false,
  externals,
  resolve,
  ...commonConfig,
}

/**
 * Embeddable yfiles-jupyter-graphs bundle
 *
 * This bundle is almost identical to the notebook extension bundle. The only
 * difference is in the configuration of the webpack public path for the
 * static assets.
 *
 * The target bundle is always `dist/index.js`, which is the path required by
 * the custom widget embedder.
 */
const embeddableNotebookBundle = {
  entry: './src/index.ts',
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'dist'),
    libraryTarget: 'amd', // It must be an amd module
    library: 'yfiles-jupyter-graphs',
    publicPath: 'https://unpkg.com/yfiles-jupyter-graphs@' + version + '/dist/',
  },
  devtool: 'source-map',
  module: {
    rules: rules,
  },
  externals,
  resolve,
  ...commonConfig,
}

/**
 * Documentation widget bundle https://www.sphinx-doc.org/
 *
 * This bundle is used to embed widgets in the package documentation.
 */
const documentationBundle = {
  entry: './src/index.ts',
  output: {
    filename: 'embed-bundle.js',
    path: path.resolve(__dirname, 'docs', 'source', '_static'),
    library: 'yfiles-jupyter-graphs',
    libraryTarget: 'amd', // It must be an amd module
  },
  module: {
    rules: rules,
  },
  devtool: 'source-map',
  externals,
  resolve,
  ...commonConfig,
}

const bundles = [notebookBundle]

module.exports = function (env, options) {
  const isProductionBuild = options.mode === 'production'

  if (isProductionBuild) {
    console.log('Running webpack in production mode...')
    // bundles.push(embeddableNotebookBundle)
    // bundles.push(documentationBundle)

    return bundles.map((bundle) => {
      bundle.mode = options.mode

      bundle.optimization = {
        minimizer: [
          // don't minimize the yfiles chunk to save some time
          // (yfiles is already minimized)
          new TerserPlugin({
            exclude: /^yfiles\./,
            extractComments: false,
          }),
        ],
      }

      if (!bundle.plugins) {
        bundle.plugins = []
      }
      bundle.plugins.unshift(
        new OptimizerPlugin({
          logLevel: 'info',
          blacklist: OptimizerBlacklist,
        })
      )
      bundle.devtool = false
      return bundle
    })
  } else {
    console.log('Running webpack in development mode...')
    return bundles.map((bundle) => {
      bundle.mode = options.mode
      bundle.devtool = false

      if (!bundle.plugins) {
        bundle.plugins = []
      }
      bundle.plugins.push(
        new webpack.SourceMapDevToolPlugin({
          filename: '[file].map',
          // add source maps for non-library code to enable convenient debugging
          exclude: ['yfiles.js'],
        })
      )
      return bundle
    })
  }
}
