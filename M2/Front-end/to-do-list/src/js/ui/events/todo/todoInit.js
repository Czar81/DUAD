import { bindLogoutEvents } from "./logoutEvents.js";
import { bindAddTaskEvents } from "./addTaskEvents.js";
import { bindTaskToggleEvents } from "./taskToggleEvents.js";
import { bindTaskDeleteEvents } from "./taskDeleteEvents.js";
import { bindFilterEvents } from "./filterEvents.js";

export const bindToDoEvents = () => {
  bindLogoutEvents();
  bindAddTaskEvents();
  bindTaskToggleEvents();
  bindTaskDeleteEvents();
  bindFilterEvents();
};
