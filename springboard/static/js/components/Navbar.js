/*eslint indent: [2, 2]*/
import React from "react";

module.exports = React.createClass({
  render: function() {
    return (
      <nav className="navbar navbar-default navbar-fixed-top">
        <div className="container-fluid">
          <div className="navbar-header">
            <a className="navbar-brand" href="/">SPRINGBOARD</a>
          </div>
          <div id="navbar" className="navbar-collapse collapse">
            <ul className="nav navbar-nav navbar-right">
              <li><a href="../navbar/">Filters +</a></li>
              <li><a href="../navbar/">Fav +</a></li>
            </ul>
          </div>
        </div>
      </nav>
    );
  }
});
