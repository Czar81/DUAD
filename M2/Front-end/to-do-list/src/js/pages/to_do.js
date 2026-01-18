import { bindToDoEvents } from "../ui/events.js";
import { checkSession } from "../services/authService.js";
import { getCookie } from "../utils/cookie.js";
import { getUser } from "../services/userService.js";
import { renderUserName } from "../ui/render.js";

export const initToDoListPage = async () => {
  const uid = getCookie("uid");
  if (!uid) {
    window.location.replace("/M2/Front-end/to-do-list/src/pages/login.html");
  }
  const isValid = checkSession(uid);
  if (!isValid) {
    window.location.replace("/M2/Front-end/to-do-list/src/pages/login.html");
  }
  const user = await getUser(uid)
  if (user?.name) {
    renderUserName(user?.name)
  }
  bindToDoEvents(); 
};
