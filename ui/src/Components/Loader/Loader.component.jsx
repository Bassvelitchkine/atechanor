import React, { Fragment } from "react";
import "./Loader.css";

const Loader = () => {
  return (
    <Fragment>
      <div className="cont">
        <div className="paper"></div>
        <button>
          <div className="loader">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
          Loading
        </button>
        <div className="g-cont">
          <div className="garbage"></div>
          <div className="garbage"></div>
          <div className="garbage"></div>
          <div className="garbage"></div>
          <div className="garbage"></div>
          <div className="garbage"></div>
          <div className="garbage"></div>
          <div className="garbage"></div>
        </div>
      </div>
    </Fragment>
  );
};

export default Loader;
