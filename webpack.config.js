module.exports = {
    entry: "./springboard/static/js/app.js",

    output: {
        path: "./springboard/static/",
        filename: "app.bundle.js"
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
