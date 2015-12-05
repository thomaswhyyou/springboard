/*
 * Entry point for webpack to build js bundle.
 */
import React from "react";
import ReactDOM from "react-dom";

// Expose React and app root components at global window level.
// Not sure whether there's a more elegant way to do this. :|
if (window) {
    window.React = React;
    window.ReactDOM = ReactDOM;
    window.components = {
        FeedView: require('./FeedView')
    };
}
