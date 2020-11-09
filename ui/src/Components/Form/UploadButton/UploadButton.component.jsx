import React, { Fragment } from "react";
import Button from "@material-ui/core/Button";
import FormControl from "@material-ui/core/FormControl";

const Upload = ({ onUpload }) => {
  return (
    <Fragment>
      <label htmlFor="fileInput">
        <Button variant="contained" color="secondary" component="span">
          Upload
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
