import { addTaskToState } from "@state/taskState.js";
import { renderTaskStats } from "@render/taskStatsRender.js";
import { renderTask } from "@render/taskRender.js";
import { createTask } from "@services/taskService.js";
import { formatDate } from "@utils/helpers.js";

export const bindAddTaskEvents = () => {
  const btnNewTask = document.getElementById("btn-add");
  const inputNewTask = document.getElementById("input-add-task");
  const noTaskYet = document.getElementById("not-tasks");
  if (!btnNewTask) return;

  btnNewTask.addEventListener("click", async () => {
    if (!inputNewTask.value.trim()) return;
    const data = {
      name: inputNewTask.value,
      data: {
        created: formatDate(),
        completed: false,
      },
    };
    const task = await createTask(data);
    if (!task) return;
    addTaskToState(task);
    noTaskYet.hidden = true;
    inputNewTask.value = "";
    data.id = task.id;
    renderTask(data);
    renderTaskStats();
  });
};
