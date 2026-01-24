import { initLoginPage } from "@pages/login.js";
import { initSignupPage } from "@pages/signup.js";
import { initToDoListPage } from "@pages/to_do.js";
import { initAboutPage } from "@pages/about.js";
import { initIndexPage } from "@pages/index.js";

try {
  const page = document.body.dataset.page;

  switch (page) {
    case "login":
      initLoginPage();
      break;

    case "sign-up":
      initSignupPage();
      break;

    case "to-do":
      initToDoListPage();
      break;

    case "about":
      initAboutPage();
      break;

    case "index":
      initIndexPage();
      break;

    default:
      console.warn("Unknown page");
  }
} catch (err) {
  console.error(err);
}
