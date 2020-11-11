import React from "react";
import Avatar from "@material-ui/core/Avatar";
import useStyles from "./Loader.style";

const Loader = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Avatar alt="loader" src="./loader.gif" />
    </div>
  );
};

export default Loader;
