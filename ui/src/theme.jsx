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
    text: { primary: "#ffffff", secondary: "rgba(255, 255, 255, 0.7)" },
  },
  typography: {
    fontFamily: '"Recursive", sans-serif',
    h3: {
      fontFamily: "'Goldman', sans-serif",
      fontWeight: 300,
      fontSize: "2rem",
      lineHeight: 1.167,
      letterSpacing: "-0.01562em",
    },
  },
});

export default theme;
// '"Recursive"',
