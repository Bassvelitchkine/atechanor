import { ThemeProvider } from '@material-ui/core';
import React from 'react';
import ReactDOM from 'react-dom';
import Landing from './Pages/Landing';
import theme from './theme'

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
    <Landing />
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
