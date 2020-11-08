import React from "react";
import MenuItem from "@material-ui/core/MenuItem";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";

const SelectColumns = ({ columns }) => {
  return (
    <FormControl>
      <InputLabel id="columns">Column</InputLabel>
      <Select
        name="columns"
        // onChange={(e) => setValue("columns", e.target.value)}
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
