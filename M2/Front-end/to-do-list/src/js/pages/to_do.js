import { bindToDoEvents } from "@events/todo/todoInit.js";
import { checkSession } from "@services/authService.js";
import { getCookie } from "@utils/cookie.js";
import { getUser } from "@services/userService.js";
import { getTasks } from "@services/taskService.js";
import { setTasksState } from "@state/taskState.js";
import { renderTaskStats } from "@render/taskStatsRender.js";
import { renderTask } from "@render/taskRender.js";
import { renderUserName } from "@render/userRender.js";
import { openPopup } from "@popup/initPopup.js";

export const initToDoListPage = async () => {
  const uid = getCookie("uid");
  if (!uid) {
    window.location.replace("/src/pages/login.html");
  }
  const isValid = checkSession(uid);
  if (!isValid) {
    window.location.replace("/src/pages/login.html");
  }
  const user = await getUser(uid);
  if (user?.name) {
    renderUserName(user?.name);
  } else {
    openPopup({
      type: "warn",
      message: "Could render name",
    });
  }
  const tasks = await getTasks();
  setTasksState(tasks);
  if (Array.isArray(tasks) && tasks.length > 0) {
    tasks.forEach((task) => renderTask(task));
  } else {
    document.getElementById("not-tasks").hidden = false;
  }
  bindToDoEvents();
  renderTaskStats();
};
