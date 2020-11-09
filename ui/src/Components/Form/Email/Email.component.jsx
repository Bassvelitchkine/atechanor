import React from "react";
import TextField from "@material-ui/core/TextField";
import FormControl from "@material-ui/core/FormControl";

const Email = ({ register, errors }) => {
  return (
    <FormControl margin="normal" fullWidth>
      <TextField
        name="email"
        label="Email"
        margin="normal"
        inputRef={register({
          required: true,
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            message: "Invalid email address",
          },
        })}
        color="secondary"
        fullWidth
      />
      {errors.email && <p>{errors.email.message}</p>}
    </FormControl>
  );
};

export default Email;
