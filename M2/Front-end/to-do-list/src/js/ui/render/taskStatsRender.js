import { getTasksFromState } from "@state/taskState.js";
import { getTaskStats } from "@utils/helpers.js";

export const renderTaskStats = () => {
  const tasks = getTasksFromState();

  const { total, completed, pending } = getTaskStats(tasks);

  document.getElementById("total-tasks").textContent = total;
  document.getElementById("completed-tasks").textContent = completed;
  document.getElementById("pending-tasks").textContent = pending;
};
