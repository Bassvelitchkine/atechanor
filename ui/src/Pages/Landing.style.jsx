import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  container: {
    backgroundColor: "#212121",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    padding: 0,
    margin: 0,
    maxWidth: "none",
    height: "100vh",
  },
  typo: {
    width: "40%",
    marginTop: 20,
  },
  message: {
    with: "60%",
    textAlign: "center",
  },
});

export default useStyles;
