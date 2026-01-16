import { signUp, login, logout } from "../services/authService.js";

export const bindSignupEvents = () => {
  const formSignUp = document.getElementById("form-signup");
  if (!formSignUp) return;
  const btnSubmit = document.getElementById("btn-signup")
  const chkTerms = document.getElementById("terms-conditions")
  chkTerms.addEventListener("change", () => {
    btnSubmit.disabled = !chkTerms.checked;
    
  });
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
      location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html");
    }
  });
};

export const bindLoginEvents = () => {
  const formLogin = document.getElementById("form-login");
  if (!formLogin) return;
  formLogin.addEventListener("submit", async (e) => {
    e.preventDefault();
    const success = await login(e.target.uid.value);
    if (success) {
      location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html");
    }
  });
};

export const bindToDoEvents = () => {
  const btnOut = document.getElementById("btn-logout")
  if(!btnOut) return;

  btnOut.addEventListener("click", ()=>{
    logout()
    location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html");
  })
}