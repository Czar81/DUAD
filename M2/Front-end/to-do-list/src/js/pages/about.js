import { checkSession } from "../services/authService.js";
import { getCookie } from "../utils/cookie.js";

export const initAboutPage = () => {
  const uid = getCookie("uid");
  if (!uid) {
    window.location.replace("/M2/Front-end/to-do-list/src/pages/login.html");
  }
  const isValid = checkSession(uid);
  if (!isValid) {
    window.location.replace("/M2/Front-end/to-do-list/src/pages/login.html");
  }
};
