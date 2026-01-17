import apiClient from "../api/apiClient.js";
import { addTaskID, getTaskIDs, removeTaskID } from "../storage/taskStorage.js";

export const createTask = async (data) => {
  try {
    const response = await apiClient.post("/objects", data);
    if (response?.data?.id) {
      addTaskID(response.data.id);
      return response.data;
    }
    console.error("Error creating task");
    return null;
  } catch (err) {
    console.error(err);
    return null;
  }
};

export const getTasks = async () => {
  try {
    const taskIDs = getTaskIDs();
    if (taskIDs.lenght === 0) {
      return [];
    }
    const resquests = taskIDs.map((id) => apiClient.get(`/objects${id}`));
    const responses = await Promise.all(resquests);
    return responses.map((res) => res.data);
  } catch (err) {
    console.error(err);
    return [];
  }
};

export const getOneTask = async (taskID) => {
  try {
    const task = await apiClient.get(`/objects/${taskID}`);
    if (task?.data?.id) {
      return task.data;
    }
    return null;
  } catch (err) {
    console.error(err);
    return null;
  }
};

export const updateTask = async (taskID, data) => {
  try {
    const response = await apiClient.put(`/objects/${taskID}`, data);
    if (response?.data?.id) {
      return response.data;
    }
    console.error("Error updated task");
    return null;
  } catch (err) {
    console.error(err);
    return null;
  }
};

export const deleteTask = async (taskID) => {
  try {
    await apiClient.delete(`/objects/${taskID}`);
    removeTaskID(taskID);
    return taskID;
  } catch (err) {
    console.error(err);
    return null;
  }
};
