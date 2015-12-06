/*eslint indent: [2, 2]*/
import React from "react";

module.exports = React.createClass({
  // getDefaultProps: function() {
  //   return {
  //     imgsrc:
  //   }
  // },

  render: function() {
    return (
      <div className="spr-tile">
        <img src="https://s3.amazonaws.com/crawler-cache.jellolabs.com/5QoVQceuih4zlBtD/photo.jpg" height="100" width="100" />
        <div style={{background: "lightblue"}}>
          item description
        </div>
      </div>
    );
  }
});
