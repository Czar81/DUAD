import { initLoginPage } from "./pages/login.js";
import { initSignupPage } from "./pages/signup.js";
//import { initTodoPage } from "./pages/todo.js";
//import { initAboutPage } from "./pages/about.js";

const page = document.body.dataset.page;

switch (page) {
  case "login":
    initLoginPage();
    break;

  case "signup":
    initSignupPage();
    break;

  case "to-do":
    //initTodoPage();
    console.log("To-do-page")
    break;

  default:
    console.warn("Unknown page");
}
