import React from "react";
import Form from "./Form.component";
import Papa from "papaparse";
import axios from "axios";
import { connect } from "react-redux";
import {
  displayError,
  displayLoader,
  displaySucess,
} from "../../Modules/actions";

// UTILS
const arrayColumnSelection = (array, columnName) => {
  const header = array[0];
  const index = header.findIndex((elem) => elem === columnName);

  const res = array.slice(1).map((elem) => elem[index]);
  return res;
};

// CONTAINER
class FormContainer extends React.Component {
  state = {
    columns: ["undefined"],
    data: null,
  };

  handleCsvParsing = (file) => {
    Papa.parse(file, {
      complete: (results) => {
        this.setState({ columns: results.data[0], data: results.data });
      },
    });
  };

  onSubmit = (formData) => {
    // Display the loader
    this.props.handleLoader();

    // Prepare the data
    const profilesList = arrayColumnSelection(this.state.data, formData.column);
    const email = formData.email;
    const res = { email, profilesList };

    setTimeout(() => {
      axios({
        method: "post",
        url: `${process.env.REACT_APP_URL}:5000/submit`,
        headers: {
          "Access-Control-Allow-Origin": true,
        },
        data: res,
      })
        .then((response) => {
          this.props.handleSuccess();
        })
        .catch((err) => {
          console.log(err);
          this.props.handleError();
        });
    }, 1000);
  };

  render() {
    return (
      <Form
        csvParser={(file) => this.handleCsvParsing(file)}
        columns={this.state.columns}
        onSubmit={(data) => this.onSubmit(data)}
      />
    );
  }
}

// LINK REDUX AND REACT
const mapDispatchToProps = (dispatch) => {
  return {
    handleError: () => {
      dispatch(displayError());
    },
    handleSuccess: () => {
      dispatch(displaySucess());
    },
    handleLoader: () => {
      dispatch(displayLoader());
    },
  };
};

export default connect(null, mapDispatchToProps)(FormContainer);
