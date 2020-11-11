import { ThemeProvider } from '@material-ui/core';
import React from 'react';
import ReactDOM from 'react-dom';
import Landing from './Pages/Landing.component';
import theme from './theme'
import { Provider } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import stateManager from "./Modules/reducers"; 
import "./index.css"

// REDUX 
const loggerMiddleware = (store) => (next) => (action) => {
  console.group(action.type);
  console.info("dispatching", action);
  let result = next(action);
  console.log("next state", store.getState());
  console.groupEnd();
  return result;
};

const store = createStore(
  stateManager,
  applyMiddleware(
    loggerMiddleware // to display the logs in the console
  )
);

// REACT Rendering
ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
    <ThemeProvider theme={theme}>
    <Landing />
    </ThemeProvider>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
