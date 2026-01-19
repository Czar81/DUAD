import { signUp } from "@services/authService.js";

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
        location.replace("/src/pages/to-do.html");
      }
    } catch (err) {
      console.error("Signup failed: ", err);
    }
  });
};
