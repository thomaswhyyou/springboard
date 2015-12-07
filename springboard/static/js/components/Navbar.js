/*eslint indent: [2, 2]*/
import React from "react";

module.exports = React.createClass({
  render: function() {
    return (
      <nav id="spr-navbar" className="navbar navbar-default navbar-fixed-top">
        <div className="container-fluid">
          <div className="navbar-header">
            <a className="navbar-brand" href="/">SPRINGBOARD</a>
          </div>
          <div>
            <ul className="nav navbar-nav navbar-right">
              <li><a href="">+ Filters</a></li>
              <li><a href="../navbar/">My Board</a></li>
            </ul>
          </div>
        </div>
        <div id="spr-filter-section" className="container-fluid">
          <div>
            asdf
          </div>
        </div>
      </nav>
    );
  }
});
