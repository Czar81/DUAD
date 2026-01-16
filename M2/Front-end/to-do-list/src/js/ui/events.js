import { signUp, login } from "../services/authService.js";

export const bindSignupEvents = () => {
  const formSignUp = document.getElementById("form-signup");
  if (!formSignUp) {
    return;
  }

  formSignUp.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: e.target.name.value,
      data: {
        lastname: e.target.lastName.value,
        email: e.target.email.value,
        password: e.target.password.value,
      },
    };

    const success = await signUp(data);
    if (success) {
      window.location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html");
    }
  });
};
