import apiClient from "../api/apiClient.js";

export const getUser = async (uid) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (response?.data?.id) {
      return response.data;
    }
    return {};
  } catch (err) {
    console.error(err);
    return {};
  }
};
