import React from "react";
import Form from "./Form.component";
import Papa from "papaparse";
import axios from "axios";

const arrayColumnSelection = (array, columnName) => {
  const header = array[0];
  const index = header.findIndex((elem) => elem === columnName);

  const res = array.slice(1).map((elem) => elem[index]);
  return res;
};

export default class FormContainer extends React.Component {
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
    const profilesList = arrayColumnSelection(this.state.data, formData.column);
    const email = formData.email;
    const res = { email, profilesList };

    axios({
      method: "post",
      url: "http://192.168.99.100:5000/submit",
      headers: {
        "Access-Control-Allow-Origin": true,
      },
      data: res,
    })
      .then((response) => {
        console.log("Successful submission");
      })
      .catch((err) => console.log(err));
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
