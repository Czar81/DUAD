import { getPendingTask, getCompletedTask } from "@utils/helpers.js";
import { renderTask } from "@render/taskRender.js";
import { changeBtnState } from "@render/btnFiltersRender.js";
import { getTasksFromState } from "@state/taskState.js";

export const bindFilterEvents = () => {
  const taskContainer = document.getElementById("task-container");
  const containerFilters = document.getElementById("btn-filters");
  if (containerFilters) {
    containerFilters.addEventListener("click", (e) => {
      const btn = e.target.closest("button");
      if (!btn) return;
      let tasks = [];
      taskContainer.innerHTML = "";
      const taskFromState = getTasksFromState();
      if (btn.id === "btn-get-all") {
        tasks = taskFromState;
      } else if (btn.id === "btn-get-pending") {
        tasks = getPendingTask(taskFromState);
      } else if (btn.id === "btn-get-completed") {
        tasks = getCompletedTask(taskFromState);
      }
      tasks.forEach((task) => renderTask(task));
      changeBtnState(containerFilters, btn);
    });
  }
};
