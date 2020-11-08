import React, { Fragment } from "react";
import TextField from "@material-ui/core/TextField";

const Email = ({ register, errors }) => {
  return (
    <Fragment>
      <TextField
        name="email"
        label="email"
        margin="normal"
        inputRef={register({
          required: true,
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            message: "Invalid email address",
          },
        })}
        fullWidth
      />
      {errors.email && <p>{errors.email.message}</p>}
    </Fragment>
  );
};

export default Email;
