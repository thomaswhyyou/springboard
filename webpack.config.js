module.exports = {
    entry: "./springboard/static/entry.js",

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
        }, {
            test: /\.scss$/,
            loaders: ["style", "css", "sass"]
        }]
    },

    resolve: {
        extensions: ['', '.js', '.json', '.jsx']
    }
};
