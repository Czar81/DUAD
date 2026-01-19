import { signUp, login, logout } from "../services/authService.js";
import {
  createTask,
  getOneTask,
  updateTask,
  deleteTask,
} from "../services/taskService.js";
import {
  formatDate,
  getPendingTask,
  getCompletedTask,
} from "../utils/helpers.js";
import { renderTask, renderTaskStats, changeBtnState } from "./render.js";
import {
  addTaskToState,
  updateTaskInState,
  getTasksFromState,
  removeTaskFromState,
} from "../state/taskState.js";

export const bindSignupEvents = () => {
  const formSignUp = document.getElementById("form-signup");
  if (!formSignUp) return;
  const btnSubmit = document.getElementById("btn-signup");
  const chkTerms = document.getElementById("terms-conditions");
  chkTerms.addEventListener("change", () => {
    btnSubmit.disabled = !chkTerms.checked;
  });
  formSignUp.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: e.target.name.value,
      data: {
        lastname: e.target.lastName.value,
        email: e.target.email.value,
        password: e.target.password.value,
      },
    };

    const success = await signUp(data);
    if (success) {
      location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html");
    }
  });
};

export const bindLoginEvents = () => {
  const formLogin = document.getElementById("form-login");
  if (!formLogin) return;
  formLogin.addEventListener("submit", async (e) => {
    e.preventDefault();
    const success = await login(e.target.uid.value, e.target.password.value);
    if (success) {
      location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html");
    }
    return;
  });
};

export const bindToDoEvents = () => {
  const btnOut = document.getElementById("btn-logout");
  const btnNewTask = document.getElementById("btn-add");
  const inputNewTask = document.getElementById("input-add-task");
  const taskContainer = document.getElementById("task-container");
  const noTaskYet = document.getElementById("not-tasks");
  const containerFilters = document.getElementById("btn-filters");

  if (!btnOut) return;

  btnOut.addEventListener("click", () => {
    logout();
    location.replace("/M2/Front-end/to-do-list/src/pages/login.html");
  });

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
  if (!taskContainer) return;
  taskContainer.addEventListener("change", async (e) => {
    if (e.target.classList.contains("check-task")) {
      const task = e.target.closest(".task-card");
      task.classList.toggle("completed", e.target.checked);
      const actualTask = await getOneTask(task.dataset.id);
      actualTask.data.completed = e.target.checked;
      await updateTask(task.dataset.id, actualTask);
      updateTaskInState(task.dataset.id, e.target.checked);
    }
  });

  taskContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("btn-delete")) {
      const task = e.target.closest(".task-card");
      deleteTask(task.dataset.id);
      task.remove();
      if (task.children.length === 2) {
        noTaskYet.hidden = false;
      }
      removeTaskFromState(task.dataset.id);
    }
  });
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
