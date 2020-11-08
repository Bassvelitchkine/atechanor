import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";

const Submit = () => {
  return (
    <Fragment>
      <label htmlFor="submitButton">
        <Button variant="contained" color="primary" component="span">
          Submit
        </Button>
      </label>
      <input type="submit" id="submitButton" style={{ display: "none" }} />
    </Fragment>
  );
};

export default Submit;
