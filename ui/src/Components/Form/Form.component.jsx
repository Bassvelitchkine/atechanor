import Email from "./Email/Email.component";
import UploadButton from "./UploadButton/UploadButton.component";
import SubmitButton from "./SubmitButton/SubmitButton.component";
import SelectColumns from "./SelectColumns/SelectColumns.component";
import { useForm } from "react-hook-form";
import useStyles from "./Form.style";
import { Typography } from "@material-ui/core";

const Form = ({ csvParser, columns, onSubmit, status }) => {
  const { register, errors, handleSubmit, setValue } = useForm();
  const classes = useStyles();

  const handleChange = (e) => {
    let files = e.target.files;
    csvParser(files[0]);
  };

  switch (status) {
    case "LOADING":
      return <Typography>Loading</Typography>;
    case "ERROR":
      return <Typography>Error</Typography>;
    case "SUCCESS":
      return <Typography>Success</Typography>;
    default:
      return (
        <form onSubmit={handleSubmit(onSubmit)} className={classes.form}>
          <UploadButton onUpload={(e) => handleChange(e)} />
          <SelectColumns
            columns={columns}
            register={register}
            setValue={setValue}
          />
          <Email register={register} errors={errors} />
          <SubmitButton />
        </form>
      );
  }
};

export default Form;
