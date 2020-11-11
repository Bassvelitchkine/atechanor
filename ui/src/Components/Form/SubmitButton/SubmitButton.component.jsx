import React from "react";
import Button from "@material-ui/core/Button";
import useStyles from "./SubmitButton.style";

const Submit = () => {
  const classes = useStyles();
  return (
    <Button type="submit" className={classes.submitButton} size="large">
      Submit
    </Button>
  );
};

export default Submit;
