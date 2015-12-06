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
            exclude: /node_modules/,
            loaders: ["style", "css", "sass"]
        }, {
            // https://github.com/metafizzy/isotope/issues/979
            test: /isotope\-|fizzy\-ui\-utils|desandro\-|masonry|outlayer|get\-size|doc\-ready|eventie|eventemitter/,
            loader: "imports?define=>false&this=>window"
        }]
    },

    resolve: {
        extensions: ['', '.js', '.json', '.jsx']
    }
};
