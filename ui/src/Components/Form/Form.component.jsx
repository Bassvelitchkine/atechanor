import Email from "./Email/Email.component";
import UploadButton from "./UploadButton/UploadButton.component";
import SubmitButton from "./SubmitButton/SubmitButton.component";
import SelectColumns from "./SelectColumns/SelectColumns.component";
import { useForm } from "react-hook-form";

const Form = () => {
  const { register, errors } = useForm();
  const columns = ["column1", "column2"];
  return (
    <form>
      <UploadButton />
      <br />
      <SelectColumns columns={columns} />
      <br />
      <Email register={register} errors={errors} />
      <br />
      <SubmitButton />
    </form>
  );
};

export default Form;
