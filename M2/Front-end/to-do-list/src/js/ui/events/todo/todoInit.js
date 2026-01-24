import { bindLogoutEvents } from "./logoutEvents.js";
import { bindAddTaskEvents } from "./addTaskEvents.js";
import { bindTaskToggleEvents } from "./taskToggleEvents.js";
import { bindTaskDeleteEvents } from "./taskDeleteEvents.js";
import { bindFilterEvents } from "./filterEvents.js";
import { bindProfileEvents } from "./profileEvents.js";
import { openPopup } from "@popup/initPopup.js";

export const bindToDoEvents = () => {
  try {
    bindLogoutEvents();
    bindAddTaskEvents();
    bindTaskToggleEvents();
    bindTaskDeleteEvents();
    bindFilterEvents();
    bindProfileEvents();
  } catch (err) {
    console.log(err);
    openPopup({ type: "error", message: `Unexpected error: ${err.message}` });
  }
};
