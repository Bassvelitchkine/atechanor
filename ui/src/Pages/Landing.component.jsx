import React from "react";
import FormContainer from "../Components/Form/Form.container";
import Container from "@material-ui/core/Container";
import useStyles from "./Landing.style";
import Typography from "@material-ui/core/Typography";

const Landing = () => {
  const classes = useStyles();
  return (
    <Container disableGutters={true} className={classes.container}>
      <Typography className={classes.typo} color="textPrimary" align="center">
        Upload a csv file with links to the stackoverflow profiles of which
        you're trying to find the emails
      </Typography>
      <FormContainer />
    </Container>
  );
};

export default Landing;
