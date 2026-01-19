export const renderUserName = (name) => {
  const display = document.getElementById("name-log");
  if (!display) return;
  display.textContent = name;
};
