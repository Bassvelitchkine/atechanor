import React from "react";
import FormContainer from "../Components/Form/Form.container";
import Container from "@material-ui/core/Container";
import useStyles from "./Landing.style";
import Typography from "@material-ui/core/Typography";

const Landing = ({ status }) => {
  const classes = useStyles();
  var component = null;
  switch (status) {
    case "LOADING":
      component = <Typography>Loading</Typography>;
      break;
    case "ERROR":
      component = <Typography>Error</Typography>;
      break;
    case "SUCCESS":
      component = <Typography>Success</Typography>;
      break;
    default:
      component = <FormContainer />;
  }

  return (
    <Container disableGutters={true} className={classes.container}>
      <Typography className={classes.typo} color="textPrimary" align="center">
        Upload a csv file with links to the stackoverflow profiles of which
        you're trying to find the emails
      </Typography>
      {component}
    </Container>
  );
};

export default Landing;
