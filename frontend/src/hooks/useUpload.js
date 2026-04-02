import { useState } from "react";

const useUpload = () => {
  const [loading, setLoading] = useState(false);

  return { loading, setLoading };
};

export default useUpload;
