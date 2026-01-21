export const renderTask = (data) => {
  const taskContainer = document.getElementById("task-container");

  const li = document.createElement("li");
  const taskContent = document.createElement("div");
  taskContent.className = "task-content";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "check-task";

  const taskDesc = document.createElement("div");
  taskDesc.className = "task-desc";

  const taskText = document.createElement("p");
  taskText.className = "task-text";
  taskText.textContent = data.name;

  const taskDate = document.createElement("p");
  taskDate.className = "task-date";
  taskDate.textContent = `Created: ${data.data.created}`;

  const btnDelete = document.createElement("button");
  btnDelete.className = "btn-delete";
  btnDelete.textContent = "Delete";
  if (data.data.completed) {
    li.className = "task-card completed";
    checkbox.checked = true;
  } else {
    li.className = "task-card";
  }
  li.dataset.id = data.id;

  taskDesc.append(taskText, taskDate);
  taskContent.append(checkbox, taskDesc);
  li.append(taskContent, btnDelete);
  taskContainer.appendChild(li);
};

export const renderNoTask = (type) => {
  const container = document.getElementById("task-container");
  const noTask = document.createElement("li")
  noTask.id="not-tasks"
  const messages = {
    all: "No tasks yet",
    pending: "No tasks pending",
    completed: "No tasks completed",
  };

  noTask.textContent = messages[type] ?? "Unknown type";
  container.appendChild(noTask)
};

export const hiddeNoTask = () => {
  const noTaskYet = document.getElementById("not-tasks");
  noTaskYet.remove()
};
