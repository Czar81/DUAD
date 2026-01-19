import { getOneTask, updateTask } from "@services/taskService.js";
import { updateTaskInState } from "@state/taskState.js";
import { renderTaskStats } from "@render/taskStatsRender.js";

export const bindTaskToggleEvents = () => {
  const taskContainer = document.getElementById("task-container");
  if (!taskContainer) return;
  taskContainer.addEventListener("change", async (e) => {
    if (e.target.classList.contains("check-task")) {
      const task = e.target.closest(".task-card");
      task.classList.toggle("completed", e.target.checked);
      const actualTask = await getOneTask(task.dataset.id);
      actualTask.data.completed = e.target.checked;
      await updateTask(task.dataset.id, actualTask);
      updateTaskInState(task.dataset.id, e.target.checked);
      renderTaskStats();
    }
  });
};
