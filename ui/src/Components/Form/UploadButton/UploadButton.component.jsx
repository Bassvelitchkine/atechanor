import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";

const Upload = ({ onUpload }) => {
  return (
    <Fragment>
      <label htmlFor="fileInput">
        <Button variant="contained" color="primary" component="span">
          Upload your .csv
        </Button>
      </label>
      <input
        accept=".csv"
        id="fileInput"
        name="file"
        type="file"
        style={{ display: "none" }}
        onChange={(e) => onUpload(e)}
      />
    </Fragment>
  );
};

export default Upload;
