import {
  LOADING,
  SUCCESS,
  ERROR,
} from "./actions";

// We need to handle the actions that deal with the fetching part of the state
export default function stateManager(
  state = {
    status: "PENDING"
  },
  action
) {
  switch (action.type) {
    case LOADING:
      return Object.assign({}, state, { status: "LOADING" });
    case ERROR:
      return Object.assign({}, state, { status: "ERROR" });
    case SUCCESS:
      return Object.assign({}, state, { status: "SUCCESS" });
    default:
      return state;
  }
}
