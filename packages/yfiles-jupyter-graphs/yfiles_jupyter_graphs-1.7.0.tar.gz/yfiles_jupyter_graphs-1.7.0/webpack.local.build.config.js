const path = require('path')
const webpack = require('webpack')
const OptimizerPlugin = require('@yworks/optimizer/webpack-plugin')
const TerserPlugin = require('terser-webpack-plugin')
const version = require('./package.json').version
const { OptimizerBlacklist } = require('./optimizer-blacklist')

module.exports = (env) => {
  const plugins = [
    new webpack.DefinePlugin({
      __VERSION__: JSON.stringify(version),
    }),
  ]
  let optimization

  if (env.WEBPACK_SERVE) {
    plugins.push(
      new webpack.SourceMapDevToolPlugin({
        filename: '[file].map',
        // add source maps for non-library code to enable convenient debugging
        exclude: ['yfiles.js'],
      })
    )
  } else {
    plugins.push(
      new OptimizerPlugin({
        logLevel: 'info',
        blacklist: OptimizerBlacklist,
      })
    )

    optimization = {
      minimizer: [
        // don't minimize the yfiles chunk to save some time
        // (yfiles is already minimized)
        new TerserPlugin({
          exclude: /^yfiles\./,
        }),
      ],
    }
  }

  return {
    mode: env.WEBPACK_SERVE ? 'development' : 'production',
    entry: './src/local-sample/local.ts',
    devtool: false,
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          use: 'ts-loader',
          exclude: /node_modules/,
        },
        { test: /\.css$/, use: ['style-loader', 'css-loader'] },
      ],
    },
    resolve: {
      extensions: ['.tsx', '.ts', '.js'],
      alias: {
        vue$: 'vue/dist/vue.esm.js',
      },
    },
    devServer: {
      static: './dist',
      //host: '0.0.0.0',
    },
    plugins,
    optimization,
    output: {
      filename: 'local.build.js',
      path: path.resolve(__dirname, 'dist'),
    },
    target: 'web',
  }
}
