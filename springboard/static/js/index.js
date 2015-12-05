/*eslint indent: [2, 2]*/
import React from "react";

var Greeting = React.createClass({
  render: function() {
    return (
      <div className="greeting">
        Hello, {this.props.name}!
      </div>
    );
  }
});

React.render(
  <Greeting name="World"/>,
  document.getElementById("react-mount-point")
);
