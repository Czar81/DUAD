let tasksState = [];

export const setTasksState = (tasks) => {
  tasksState = Array.isArray(tasks) ? tasks : [];
};

export const addTaskToState = (task) => {
  tasksState.push(task);
};

export const updateTaskInState = (id, completed) => {
  const task = tasksState.find(t => t.id === id);
  if (task) task.data.completed = completed;
};

export const removeTaskFromState = (id) => {
  tasksState = tasksState.filter(t => t.id !== id);
};

export const getTasksFromState = () => [...tasksState];
