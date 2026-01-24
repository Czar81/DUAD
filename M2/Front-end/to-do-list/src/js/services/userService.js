import apiClient from "@api/apiClient.js";
import { openPopup } from "@popup/initPopup.js";

export const getUser = async (uid) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (response?.data?.id) {
      return response.data;
    }
    openPopup({
      type: "warn",
      message: "Could not get user data",
    });
    return {};
  } catch (err) {
    console.error(err);
    openPopup({
      type: "error",
      message: `Error trying to get user data: ${err}`,
    });
    return {};
  }
};
