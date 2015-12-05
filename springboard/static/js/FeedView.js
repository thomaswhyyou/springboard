/*eslint indent: [2, 2]*/
import React from "react";
import Navbar from "./components/Navbar";
import Board from "./components/Board";

module.exports = React.createClass({
  render: function() {
    return (
      <div>
        <Navbar />
        <Board />
      </div>
    );
  }
});
