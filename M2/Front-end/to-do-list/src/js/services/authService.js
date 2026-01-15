import apiClient from "../api/apiClient";
import { setUserId, clearUserId } from "../storage/sessionStorage";

export const signUp = async (data) => {
  try {
    const response = await apiClient.post("/objects", data);
    if (response?.data?.id) {
      setUserId(response.data.id);
      return response.data;
    }
    console.error("Error while signing up");
    return null;
  } catch (err) {
    console.error(err);
    return null;
  }
};

export const login = async (uid) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (response?.data?.id) {
      setUserId(response.data.id); 
      return response.data;
    }
    console.error("Error while logging in");
    return null;
  } catch (err) {
    console.error(err);
    return null;
  }
};

export const logout = () => {
  clearUserId();
};
