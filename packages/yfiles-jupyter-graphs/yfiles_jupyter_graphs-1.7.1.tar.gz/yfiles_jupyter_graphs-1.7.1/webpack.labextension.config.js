const webpack = require('webpack')
const OptimizerPlugin = require('@yworks/optimizer/webpack-plugin')
const TerserPlugin = require('terser-webpack-plugin')
const version = require('./package.json').version
const { OptimizerBlacklist } = require('./optimizer-blacklist')

module.exports = {
  mode: 'production',
  plugins: [
    new OptimizerPlugin({
      logLevel: 'info',
      blacklist: OptimizerBlacklist,
    }),
    new webpack.DefinePlugin({
      __VERSION__: JSON.stringify(version),
    }),
  ],
  optimization: {
    minimizer: [
      // don't minimize the yfiles chunk to save some time
      // (yfiles is already minimized)
      new TerserPlugin({
        exclude: /^yfiles\./,
        extractComments: false,
      }),
    ],
  },
  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js',
    },
  },
}
