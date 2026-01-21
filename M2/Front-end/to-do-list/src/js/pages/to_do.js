import { bindToDoEvents } from "@events/todo/todoInit.js";
import { checkSession } from "@services/authService.js";
import { getCookie } from "@utils/cookie.js";
import { getUser } from "@services/userService.js";
import { getTasks } from "@services/taskService.js";
import { setTasksState } from "@state/taskState.js";
import { renderTaskStats } from "@render/taskStatsRender.js";
import { renderTask, renderNoTask } from "@render/taskRender.js";
import { renderUserName } from "@render/userRender.js";
import { openPopup } from "@popup/initPopup.js";
import { setUserState } from "@state/userState.js"

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
    setUserState(user)
  } else {
    openPopup({
      type: "warn",
      message: "Could set user",
    });
  }
  const tasks = await getTasks();
  if (Array.isArray(tasks) && tasks.length > 0) {
    setTasksState(tasks);
    tasks.forEach((task) => renderTask(task));
  } else {
    renderNoTask("all")
  }
  bindToDoEvents();
  renderTaskStats();
};
