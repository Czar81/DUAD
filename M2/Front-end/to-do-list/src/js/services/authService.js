import apiClient from "../api/apiClient";
import { setUserId, clearUserId } from "../storage/sessionStorage";

export const signUp = async (data) => {
  try {
    const response = await apiClient.post("/objects", data);
    if (response) {
      setUserId(response.data.id);
      return response.data.id;
    }
  } catch (err) {
    console.error(err);
    return null;
  }
};

export const login = async (uid) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (response) {
      setUserId(response.data.id);
      return response.data.id;
    }
  } catch (error) {
    console.error(err);
    return null;
  }
};

export const logout = () => {
  clearUserId();
};
