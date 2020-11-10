import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";
import useStyles from "./SubmitButton.style";

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
