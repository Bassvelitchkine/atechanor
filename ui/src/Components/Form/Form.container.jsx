import React from "react";
import Form from "./Form.component";
import Papa from "papaparse";

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
    const profileUrls = arrayColumnSelection(this.state.data, formData.column);
    const email = formData.email;
    const res = { email, profileUrls };
    console.log(res);
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
