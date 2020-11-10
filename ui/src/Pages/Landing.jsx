import React from "react";
import FormContainer from "../Components/Form/Form.container";
import Container from "@material-ui/core/Container";
import useStyles from "./Landing.style";

const Landing = () => {
  const classes = useStyles();
  return (
    <Container disableGutters={true} className={classes.container}>
      <FormContainer />
    </Container>
  );
};

export default Landing;
