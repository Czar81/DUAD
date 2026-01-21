import { signUp } from "@services/authService.js";
import { openPopup } from "@popup/initPopup.js";

export const bindSignupEvents = () => {
  const formSignUp = document.getElementById("form-signup");
  if (!formSignUp) return;
  const btnSubmit = document.getElementById("btn-signup");
  const chkTerms = document.getElementById("terms-conditions");

  chkTerms.addEventListener("change", () => {
    btnSubmit.disabled = !chkTerms.checked;
  });
  formSignUp.addEventListener("submit", async (e) => {
    e.preventDefault();
    const { name, lastName, email, password } = e.target.elements;

    if (
      !name.value.trim() ||
      !lastName.value.trim() ||
      !email.value.trim() ||
      !password.value.trim()
    ) {
      openPopup({
        type: "warn",
        message: "Uno o más inputs estan vacios",
      });
      return;
    }

    const data = {
      name: name.value,
      data: {
        lastname: lastName.value,
        email: email.value,
        password: password.value,
      },
    };

    try {
      const success = await signUp(data);

      if (success) {
        openPopup({
          type: "success",
          message: `User created, id: ${success.id}`,
        });
        setTimeout(() => {
          location.replace("/src/pages/to-do.html");
        }, 5000);
      }
    } catch (err) {
      console.error("Signup failed: ", err);
      openPopup({
        type: "error",
        message: `Error signup ${err.message}`,
      });
    }
  });
};
