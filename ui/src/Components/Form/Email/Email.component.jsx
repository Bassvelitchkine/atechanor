import React from "react";
import TextField from "@material-ui/core/TextField";
import FormControl from "@material-ui/core/FormControl";
import FormHelperText from "@material-ui/core/FormHelperText";

const Email = ({ register, errors }) => {
  return (
    <FormControl margin="normal" fullWidth>
      <TextField
        name="email"
        label="Your email"
        margin="normal"
        inputRef={register({
          required: true,
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            message: "Invalid email address",
          },
        })}
        color="primary"
        variant="outlined"
        size="medium"
      />
      {errors.email && <FormHelperText>{errors.email.message}</FormHelperText>}
    </FormControl>
  );
};

export default Email;
