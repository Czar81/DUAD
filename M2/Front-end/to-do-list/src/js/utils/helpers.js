export const formatDate = (date = new Date()) => {
  return new Intl.DateTimeFormat("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
  }).format(date);
};

export const getTaskStats = (tasks) => {
  let total = 0;
  let completed = 0;
  let pending = 0;

  tasks.forEach(task => {
    total++;
    if (task.data.completed) {
      completed++;
    } else {
      pending++;
    }
  });

  return { total, completed, pending };
};
