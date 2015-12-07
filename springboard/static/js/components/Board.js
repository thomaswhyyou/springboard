/*eslint indent: [2, 2]*/
import React from "react";
// import ReactDOM from "react-dom";
import Tile from "./Tile";
import _ from "lodash";
import Masonry from "masonry-layout";
import request from "reqwest";
import imagesloaded from "imagesloaded";
import Waypoint from "react-waypoint";


module.exports = React.createClass({
  getDefaultProps: function() {
    return {
      urlForProducts: "/api/products"
    };
  },

  getInitialState: function() {
    return {
      products: [],
      nextOffset: 0,
      isLoading: true
    };
  },

  _fetchProductData: function() {
    this.setState({ isLoading: true });

    var self = this;
    request({
      url: self.props.urlForProducts,
      method: "GET",
      data: {
        offset: self.state.nextOffset
      },
      success: function(resp) {
        self.setState({
          products: self.state.products.concat(resp.data),
          nextOffset: parseInt(resp.offset) + 1
        });

        var board = document.querySelector("#spr-board");
        imagesloaded(board, function() {
          new Masonry(board, {
            columnWidth: '.spr-tile',
            gutter: 10,
            transitionDuration: "0.2s",
            itemSelector: ".spr-tile"
          });

          self.setState({ isLoading: false });
        });
      }
    });
  },

  _handleWaypointEnter: function() {
    this._fetchProductData();
  },

  componentDidMount: function() {
    this._fetchProductData();
  },

  render: function() {
    return (
      <div id="spr-board">
        {_.map(this.state.products, function(product) {
          return (
            <Tile key={product.id}
                  photoUrl={product.photo_url}
                  productName={product.name}
                  vendorName={product.vendor_name}
                  description={product.description}
                  category={product.category}
                  targetGender={product.target_gender}
                  price={product.price}
                  isOnSale={product.is_on_sale}
            />
          );
        }, this)}

        <div className="spr-tile spr-board-end">
          {!this.state.isLoading &&
            <Waypoint onEnter={this._handleWaypointEnter} threshold={0.2} />}
          {this.state.isLoading &&
            <i className="fa fa-spinner fa-2x fa-spin"></i>}
        </div>
      </div>
    );
  }
});
