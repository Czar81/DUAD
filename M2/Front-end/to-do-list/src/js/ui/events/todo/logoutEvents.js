import { logout } from "@services/authService.js";
import { openPopup } from "@popup/initPopup.js";

export const bindLogoutEvents = () => {
  const btnOut = document.getElementById("btn-logout");
  if (!btnOut) return;

  btnOut.addEventListener("click", () => {
    openPopup({
      type: "info",
      message: "Cerrando sesion bye",
    });
    logout();
    setTimeout(() => {
      location.replace("/src/pages/login.html");
    }, 5000);
  });
};
