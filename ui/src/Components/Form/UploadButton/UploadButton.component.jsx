import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";

const Upload = () => {
  return (
    <Fragment>
      <label htmlFor="fileInput">
        <Button variant="contained" color="primary" component="span">
          Upload
        </Button>
      </label>
      <input
        accept=".csv"
        id="fileInput"
        name="file"
        type="file"
        style={{ display: "none" }}
      />
    </Fragment>
  );
};

export default Upload;
