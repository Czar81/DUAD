export const getTaskIDs = () =>
  JSON.parse(localStorage.getItem("taskIDs")) || [];

export const addTaskID = (taskID) => {
  const ids = getTaskIDs();
  if (!ids.includes(taskID)) {
    localStorage.setItem("taskIDs", JSON.stringify([...ids, taskID]));
  }
};

export const removeTaskID = (id) => {
  const ids = getTaskIDs().filter((i) => i !== id);
  localStorage.setItem("taskIDs", JSON.stringify(ids));
};
