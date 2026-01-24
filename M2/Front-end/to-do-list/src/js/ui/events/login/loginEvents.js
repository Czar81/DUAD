import { login } from "@services/authService.js";
import { openPopup } from "@popup/initPopup.js";

export const bindLoginEvents = () => {
  const formLogin = document.getElementById("form-login");
  if (!formLogin) return;
  formLogin.addEventListener("submit", async (e) => {
    e.preventDefault();
    try {
      const { uid, password } = e.target.elements;


      if (!uid.value.trim() || !password.value.trim()) {
        openPopup({
          type: "warn",
          message: "One or more inputs are blank",
        });
        return;
      }
      const success = await login(uid.value, password.value);
      if (success) {
        openPopup({
          type: "success",
          message: `Success login, id: ${success.id}`,
        });
        setTimeout(() => {
          location.replace("/src/pages/to-do.html");
        }, 5000);
      }
      return;
    } catch (err) {
      console.error(err);
      openPopup({
        type: "error",
        message: `Error login ${err.message}`,
      });
    }
  });
};
