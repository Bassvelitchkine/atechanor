import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  submitButton: {
    background: "linear-gradient(45deg, #ff5768 30%, #ff933c 90%)",
    border: 0,
    borderRadius: 3,
    boxShadow: "0 3px 5px 2px rgba(255, 105, 135, .3)",
    color: "white",
    height: 48,
    padding: "0 30px",
    marginTop: 100,
  },
});

const Submit = () => {
  const classes = useStyles();
  return (
    <Fragment>
      <label htmlFor="submitButton">
        <Button className={classes.submitButton} size="large">
          Submit
        </Button>
      </label>
      <input type="submit" id="submitButton" style={{ display: "none" }} />
    </Fragment>
  );
};

export default Submit;
