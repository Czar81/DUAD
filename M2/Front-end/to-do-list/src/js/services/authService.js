import apiClient from "@api/apiClient.js";
import { openPopup } from "@popup/initPopup.js";
import { setUserId, clearUserId } from "@storage/sessionStorage.js";

export const signUp = async (data) => {
  try {
    const response = await apiClient.post("/objects", data);
    if (response?.data?.id) {
      setUserId(response.data.id);
      return response.data;
    }
    openPopup({
      type: "error",
      message: "Error while signing up",
    });
    return false;
  } catch (err) {
    console.error(err);
    openPopup({
      type: "error",
      message: `Error signing up: ${err.message}`,
    });
    return false;
  }
};

export const login = async (uid, password) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (!response?.data?.id) {
      return false;
    }
    if (password === response.data.data.password) {
      setUserId(response.data.id);
      return response.data;
    } else {
      return false;
    }
  } catch (err) {
    console.error(err);
    openPopup({
      type: "error",
      message: `Error login: ${err.message}`,
    });
    return false;
  }
};

export const checkSession = async (uid) => {
  try {
    const response = await apiClient.get(`/objects/${uid}`);
    if (response?.data?.id) {
      return true;
    }
    return false;
  } catch (err) {
    console.error(err);
    return false;
  }
};

export const logout = () => {
  clearUserId();
};
