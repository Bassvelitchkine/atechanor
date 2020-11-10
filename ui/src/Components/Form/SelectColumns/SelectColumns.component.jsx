import React from "react";
import MenuItem from "@material-ui/core/MenuItem";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";

const SelectColumns = ({ columns, register, setValue }) => {
  React.useEffect(() => {
    register({ name: "column", required: true });
  }, [register]);

  return (
    <FormControl margin="normal" fullWidth>
      <InputLabel color="primary">Profile URL column</InputLabel>
      <Select
        name="column"
        onChange={(e) => setValue("column", e.target.value)}
        color="primary"
        fullWidth
      >
        {columns.map((column) => (
          <MenuItem key={column} value={column}>
            {column}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default SelectColumns;
