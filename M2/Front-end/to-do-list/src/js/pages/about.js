import { checkSession } from "@services/authService.js";
import { getCookie } from "@utils/cookie.js";

export const initAboutPage = () => {
  const uid = getCookie("uid");
  if (!uid) {
    window.location.replace("/src/pages/login.html");
  }
  const isValid = checkSession(uid);
  if (!isValid) {
    window.location.replace("/src/pages/login.html");
  }
};
