
// When we ask the api for the publications
export const LOADING = "LOADING";
export function displayLoader() {
  return {
    type: LOADING,
  };
}

// The asynchronous action creator to actually ask the publications to the api and handle the response
export const SUCCESS = "SUCCESS";
export function displaySucess() {
  return {
    type: SUCCESS,
  };
}

export const ERROR = "ERROR";
export function displayError() {
  return {
    type: ERROR,
  };
}