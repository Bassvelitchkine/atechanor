import React from "react";
import FormContainer from "../Components/Form/Form.container";
import Container from "@material-ui/core/Container";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  container: {
    backgroundColor: "#212121",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: 600,
    padding: 0,
    margin: 0,
  },
});

const Landing = () => {
  const classes = useStyles();
  return (
    <Container disableGutters={true} className={classes.container}>
      <FormContainer />
    </Container>
  );
};

export default Landing;
