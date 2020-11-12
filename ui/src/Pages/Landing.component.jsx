import React, { Fragment } from "react";
import FormContainer from "../Components/Form/Form.container";
import Container from "@material-ui/core/Container";
import useStyles from "./Landing.style";
import Typography from "@material-ui/core/Typography";
import Loader from "../Components/Loader/Loader.component";

const Landing = ({ status }) => {
  const classes = useStyles();
  var component = null;
  switch (status) {
    case "LOADING":
      component = <Loader />;
      break;
    case "ERROR":
      component = (
        <Typography
          className={classes.message}
          style={{ color: "#f44336" }}
          variant="h3"
        >
          💀 A problem occurred. Please try again later.
        </Typography>
      );
      break;
    case "SUCCESS":
      component = (
        <Typography
          className={classes.message}
          style={{ color: "#81c784" }}
          variant="h3"
        >
          🤘 You'll receive an email when your export is ready!
        </Typography>
      );
      break;
    default:
      component = (
        <Fragment>
          <Typography
            className={classes.typo}
            color="textPrimary"
            align="center"
          >
            Upload a csv file with links to the stackoverflow profiles of which
            you're trying to find the emails
          </Typography>
          <FormContainer />
        </Fragment>
      );
  }

  return (
    <Container disableGutters={true} className={classes.container}>
      {component}
    </Container>
  );
};

export default Landing;
