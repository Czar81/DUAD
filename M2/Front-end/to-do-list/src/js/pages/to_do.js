import { bindToDoEvents } from "../ui/events.js";
import { checkSession } from "../services/authService.js";
import { getCookie } from "../utils/cookie.js";
import { getUser } from "../services/userService.js";
import { renderUserName, renderTask } from "../ui/render.js";
import { getTasks } from "../services/taskService.js";

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
  const tasks = await getTasks()
  if (Array.isArray(tasks) && tasks.length > 0) {
    tasks.forEach(task => renderTask(task))
  }else{
    document.getElementById("not-tasks").hidden=false;
  }
  bindToDoEvents();
};
