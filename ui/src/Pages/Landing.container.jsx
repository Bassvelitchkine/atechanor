import React from "react";
import Landing from "./Landing.component";
import { connect } from "react-redux";

const LandingContainer = ({ status }) => <Landing status={status} />;

const mapStateToProps = (state) => {
  return {
    status: state.status,
  };
};

export default connect(mapStateToProps)(LandingContainer);
