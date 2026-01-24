import { getPendingTask, getCompletedTask } from "@utils/helpers.js";
import { renderTask, renderNoTask } from "@render/taskRender.js";
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
      let type=""
      taskContainer.innerHTML = "";
      const taskFromState = getTasksFromState();
      if (btn.id === "btn-get-all") {
        tasks = taskFromState;
        type = "all"
      } else if (btn.id === "btn-get-pending") {
        tasks = getPendingTask(taskFromState);
        type = "pending"
      } else if (btn.id === "btn-get-completed") {
        tasks = getCompletedTask(taskFromState);
        type = "completed"
      }
      if (tasks.length === 0) {
        renderNoTask(type)
      }else{
        tasks.forEach((task) => renderTask(task));
      }
      changeBtnState(containerFilters, btn);
    });
  }
};
