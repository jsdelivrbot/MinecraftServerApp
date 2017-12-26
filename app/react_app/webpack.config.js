module.exports = {
  entry: [
    'babel-polyfill',
    './src/index'
  ],
  output: {
    path: __dirname,
    publicPath: '/',
    filename: 'bundle.js'
  },
  devtool: "eval-source-map",
  module: {
    loaders: [
        {
          exclude: /node_modules/,
          loader: 'babel',
          query: {
            presets: ['react', 'es2015', 'stage-1']
          }
        },
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader : 'babel-loader',
        },
        {
          test: /\.(png|jpg|gif)$/,
          loader: "url-loader?name=react_app/images/[name].[ext]",
        },

    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  devServer: {
    historyApiFallback: true,
    contentBase: './'
  }
};
