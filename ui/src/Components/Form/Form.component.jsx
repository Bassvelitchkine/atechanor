import Email from "./Email/Email.component";
import UploadButton from "./UploadButton/UploadButton.component";
import SubmitButton from "./SubmitButton/SubmitButton.component";
import SelectColumns from "./SelectColumns/SelectColumns.component";
import { useForm } from "react-hook-form";

const Form = ({ csvParser, columns, onSubmit }) => {
  const { register, errors, handleSubmit, setValue } = useForm();

  const handleChange = (e) => {
    let files = e.target.files;
    csvParser(files[0]);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <UploadButton onUpload={(e) => handleChange(e)} />
      <br />
      <SelectColumns
        columns={columns}
        register={register}
        setValue={setValue}
      />
      <br />
      <Email register={register} errors={errors} />
      <br />
      <SubmitButton />
    </form>
  );
};

export default Form;
