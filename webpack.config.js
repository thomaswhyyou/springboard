module.exports = {
    entry: "./springboard/static/js/index.js",

    output: {
        path: "./springboard/static/",
        filename: "bundle.js"
    },

    module: {
        loaders: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: "babel",
            query: {
                presets: ['react', 'es2015']
            }
        }]
    },

    resolve: {
        extensions: ['', '.js', '.json', '.jsx']
    }
};
