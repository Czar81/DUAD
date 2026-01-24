import { deleteTask } from "@services/taskService.js";
import { removeTaskFromState } from "@state/taskState.js";
import { renderTaskStats } from "@render/taskStatsRender.js";
import { renderNoTask } from "@render/taskRender.js";
import { openPopup } from "@popup/initPopup.js";

export const bindTaskDeleteEvents = () => {
  const taskContainer = document.getElementById("task-container");
  taskContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("btn-delete")) {
      const task = e.target.closest(".task-card");
      deleteTask(task.dataset.id);
      task.remove();
      removeTaskFromState(task.dataset.id);
      if (taskContainer.children.length === 0) {
        renderNoTask("all")
      }
      renderTaskStats();
      openPopup({
        type: "info",
        message: "Tarea borrada",
      });
    }
  });
};
