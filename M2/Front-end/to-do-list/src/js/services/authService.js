import apiClient from "../api/apiClient.js";
import { setUserId, clearUserId } from "../storage/sessionStorage.js";

export const signUp = async (data) => {
  try {
    const response = await apiClient.post("/objects", data);
    if (response?.data?.id) {
      setUserId(response.data.id);
      return response.data;
    }
    console.error("Error while signing up");
    return false;
  } catch (err) {
    console.error(err);
    return false;
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
    return false;
  } catch (err) {
    console.error(err);
    return false;
  }
};

export const checkSession = async (uid) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (response?.data?.id) {
      return true
    }
    return !!response
  } catch (err) {
    console.error(err);
    return false
  }
}

export const logout = () => {
  clearUserId();
};
