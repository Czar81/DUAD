const apiClient = axios.create({
  baseURL: "https://api.restful-api.dev/",
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
