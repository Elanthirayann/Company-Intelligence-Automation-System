import { useLocation } from "react-router-dom";
import DataTable from "../components/DataTable";

const Results = () => {
  const location = useLocation();
  const data = location.state?.data || [];

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Results</h1>
      <DataTable data={data} />
    </div>
  );
};

export default Results;
