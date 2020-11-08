import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";

const Submit = () => {
  return (
    <Fragment>
      <label htmlFor="submit">
        <Button>Submit</Button>
      </label>
      <input type="submit" id="submit" style={{ display: "none" }} />
    </Fragment>
  );
};

export default Submit;
