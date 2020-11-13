import { ThemeProvider } from '@material-ui/core';
import React from 'react';
import ReactDOM from 'react-dom';
import LandingContainer from './Pages/Landing.container';
import theme from './theme'
import { Provider } from "react-redux";
import { createStore } from "redux";
import stateManager from "./Modules/reducers"; 
import "./index.css"

// // REDUX 
// const loggerMiddleware = (store) => (next) => (action) => {
//   console.group(action.type);
//   console.info("dispatching", action);
//   let result = next(action);
//   console.log("next state", store.getState());
//   console.groupEnd();
//   return result;
// };

const store = createStore(
  stateManager,
  // applyMiddleware(
  //   loggerMiddleware // to display the logs in the console
  // )
);

// REACT Rendering
ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
    <ThemeProvider theme={theme}>
    <LandingContainer />
    </ThemeProvider>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
