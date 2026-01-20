import { popup } from "@render/popupRender.js";
import {showPopupProfile} from "./profilePopup.js"

export const openPopup = ({ type, message }) => {
  switch (type) {
    case "error":
      popup("popup-error", "/src/assets/icons/error.svg", "Error", message);
      break;
    case "info":
      popup("popup-info", "/src/assets/icons/info.svg", "Info", message);
      break;
    case "warn":
      popup("popup-warn", "/src/assets/icons/warn.svg", "Warn", message);
      break;
    case "success":
      popup(
        "popup-success",
        "/src/assets/icons/success.svg",
        "Success",
        message,
      );
      break;
    default:
      console.warn("Unknow popup type");
      break;
  }
};
