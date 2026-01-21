import { addTaskToState } from "@state/taskState.js";
import { renderTaskStats } from "@render/taskStatsRender.js";
import { renderTask } from "@render/taskRender.js";
import { createTask } from "@services/taskService.js";
import { formatDate } from "@utils/helpers.js";
import { openPopup } from "@popup/initPopup.js";

export const bindAddTaskEvents = () => {
  const btnNewTask = document.getElementById("btn-add");
  const inputNewTask = document.getElementById("input-add-task");
  const noTaskYet = document.getElementById("not-tasks");
  if (!btnNewTask) return;

  btnNewTask.addEventListener("click", async () => {
    if (!inputNewTask.value.trim()){ 
      openPopup({
        type:"warn", 
        message:"La tarea no puede ser vacia"
      })
      return;
    };
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
    openPopup({
      type:"info", 
      message:"Tarea creada"
    })
  });
};
