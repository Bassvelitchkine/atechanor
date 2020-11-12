import React, { Fragment } from "react";
import useStyles from "./Loader.style";
import "./Loader.css";

const Loader = () => {
  const classes = useStyles();
  return (
    <Fragment style={classes.loader}>
      <div class="cont">
        <div class="paper"></div>
        <button>
          <div class="loader">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
          Loading
        </button>
        <div class="g-cont">
          <div class="garbage"></div>
          <div class="garbage"></div>
          <div class="garbage"></div>
          <div class="garbage"></div>
          <div class="garbage"></div>
          <div class="garbage"></div>
          <div class="garbage"></div>
          <div class="garbage"></div>
        </div>
      </div>
    </Fragment>
  );
};

export default Loader;
