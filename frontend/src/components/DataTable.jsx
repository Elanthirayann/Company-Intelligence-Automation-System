const DataTable = ({ data }) => {
  if (!data || data.length === 0) return <p>No data</p>;

  return (
    <table className="table-auto w-full border">
      <thead>
        <tr>
          {Object.keys(data[0]).map((key) => (
            <th key={key} className="border p-2">
              {key}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, i) => (
          <tr key={i}>
            {Object.values(row).map((val, j) => (
              <td key={j} className="border p-2">
                {val}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DataTable;
