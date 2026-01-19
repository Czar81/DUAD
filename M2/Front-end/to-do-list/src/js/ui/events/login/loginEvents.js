import { login } from "@services/authService.js";

export const bindLoginEvents = () => {
  const formLogin = document.getElementById("form-login");
  if (!formLogin) return;
  formLogin.addEventListener("submit", async (e) => {
    e.preventDefault();
    const success = await login(e.target.uid.value, e.target.password.value);
    if (success) {
      location.replace("/src/pages/to-do.html");
    }
    return;
  });
};
