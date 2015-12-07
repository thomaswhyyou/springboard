/*eslint indent: [2, 2]*/
import React from "react";

module.exports = React.createClass({
  _handleClickOnFilters: function() {
    alert("Sorry, not implemented yet. SOON :|");
  },

  _handleClickOnMyBoard: function() {
    alert("Sorry, not implemented yet. SOON :|");
  },

  render: function() {
    return (
      <nav id="spr-navbar" className="navbar navbar-default navbar-fixed-top">
        <div className="container-fluid">
          <div className="navbar-header">
            <a className="navbar-brand" href="/">SPRINGBOARD</a>
          </div>
          <div>
            <ul className="nav navbar-nav navbar-right">
              <li>
                <a href="javascript:void(null)"
                   onClick={this._handleClickOnFilters}>
                  + Filters
                </a>
              </li>
              <li>
                <a href="javascript:void(null)"
                   style={{paddingRight: '25px'}}
                   onClick={this._handleClickOnMyBoard}>
                  My Board
                </a>
              </li>
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
