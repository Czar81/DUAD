import { bindToDoListEvents } from "../ui/events.js";
import { checkSession } from "../services/authService.js";
import { getCookie } from "../utils/cookie.js";

export const initToDoListPage = () => {
  const uid = getCookie("uid");
  if (!uid) {
    window.location.replace("../../pages/login.html");
  }
  const isValid = checkSession(uid);
  if (!isValid) {
    window.location.replace("../../pages/login.html");
  }
  bindToDoListEvents();
};
