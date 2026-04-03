import FileUpload from "../components/FileUpload";
import { uploadCSV } from "../services/companyService";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  const handleUpload = async (file) => {
    try {
      const data = await uploadCSV(file);
      navigate("/results", { state: { data } });
    } catch (err) {
      console.error("Upload failed:", err);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">Upload Company CSV</h1>
      <FileUpload onUpload={handleUpload} />
    </div>
  );
};

export default Home;
