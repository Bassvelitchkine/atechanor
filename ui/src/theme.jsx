import { createMuiTheme } from "@material-ui/core/styles";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#ff5768",
    },
    secondary: {
      main: "#ff933c",
    },
    background: {
      paper: "#424242",
      default: "#303030",
    },
    type: "dark",
  },
});

export default theme;
