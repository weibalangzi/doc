
const path = require('path');
const webpack = require('webpack');
const utils = require('./utils');
const nodeExcternals = require('webpack-node-externals');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const webpackConfig = {
    target: 'node',
    entry: {
        server: path.join(utils.APP_PATH, 'src/index.js')
    },
    output: {
        filename: '[name].bundle.js',
        path: utils.DIST_PATH
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: {
                    loader: 'babel-loader'
                },
                exclude: [path.join(__dirname, './node_modules')]
            }
        ]
    },
    externals: [nodeExcternals()],
    plugin: [
        new CleanWebpackPlugin(),
        new webpack.DefinePlugin({
            'process.env': (process.env.NODE_ENV === 'production' || process.env.NODE_ENV === 'prod') ? "'production'" : 'develepoment'
        })
    ],
    node: {
        console: true,
        global: true,
        process: true,
        Buffer: false,
        __dirname: true,
        __filename: true,
        setImmediate: true,
        path: true,
    }

}

module.exports = webpackConfig;