import { logout } from "@services/authService.js";

export const bindLogoutEvents = () => {
  const btnOut = document.getElementById("btn-logout");
  if (!btnOut) return;

  btnOut.addEventListener("click", () => {
    logout();
    location.replace("/src/pages/login.html");
  });
};
