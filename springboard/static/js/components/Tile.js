/*eslint indent: [2, 2]*/
import React from "react";
import _ from "lodash";


module.exports = React.createClass({
  _handleClickOnHeartButton: function() {
    alert("Sorry, not implemented yet. SOON :|");
  },

  render: function() {
    return (
      <div className="spr-tile">
        <div className="spr-onhover-dim">
          <img className="spr-tile-image"
              src={this.props.photoUrl}
          />
          <div className="spr-gender-taxonomy spr-show-at-dim">
            <span><b>FOR</b> </span>
            <span>{this.props.targetGender}</span>
            <br/>
            <span><b>CATEGORY</b> </span>
            <span>{this.props.category}</span>
          </div>
          <div className="spr-heartit-btn spr-show-at-dim"
               onClick={this._handleClickOnHeartButton}>
            <i className="fa fa-heart"></i>
          </div>
        </div>

        <div className="spr-tile-metabox">
          <div>
            <span>{this.props.productName}</span>
            <br/>
            <span style={{color: "#DADADA", fontStyle: "italic"}}>by </span>
            <span>{this.props.vendorName}</span>
          </div>

          {!_.isEmpty(this.props.description) &&
          <div>{this.props.description}</div>}

          <div>
            <span>${this.props.price}</span>
            {
              this.props.isOnSale === true &&
              <span style={{color: "#FF0000", fontWeight: "600", float: "right"}}>
                SALE
              </span>
            }
          </div>
        </div>
      </div>
    );
  }
});
