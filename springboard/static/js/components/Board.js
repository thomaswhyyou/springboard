/*eslint indent: [2, 2]*/
import React from "react";
import ReactDOM from "react-dom";
import Tile from "./Tile";
import _ from "lodash";
import Masonry from "masonry-layout";


module.exports = React.createClass({
  componentDidMount: function() {
    // var container = document.querySelector("#spr-board");
    var masonry = new Masonry("#spr-board", {
      columnWidth: '.spr-tile',
      gutter: 10,
      transitionDuration: "0.1s",
      itemSelector: ".spr-tile"
    });
  },

  render: function() {
    var tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1,1 ,1 ,1 ,11, 1, 1, 1, 1, 1,1 ,1 ,1 ,1, 1, 1 ,1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];

    return (
      <div id="spr-board">
        This is FeedViewx

        {_.map(tiles, function() {
          return (
            <Tile />
          );
        }, this)}
      </div>
    );
  }
});
