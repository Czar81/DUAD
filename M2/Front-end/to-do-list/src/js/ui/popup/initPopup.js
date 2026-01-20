import { popup } from "./popup.js";
//import {showPopupProfile} from "./profilePopup.js"

export const openPopup = ({ type, message }) => {
  switch (type) {
    case "error":
      popup("popup-error", "Error", "/src/assets/icons/error.svg", message);
      break;
    case "info":
      popup("popup-info", "Info", "/src/assets/icons/info.svg", message);
      break;
    case "warn":
      popup("popup-warn", "Warn", "/src/assets/icons/warn.svg", message);
      break;
    case "success":
      popup(
        "popup-success",
        "Success",
        "/src/assets/icons/success.svg",
        message,
      );
      break;
    //case profile:
    //  showPopupProfile()
    //  break;
    default:
      console.warn("Unknow popup type");
      break;
  }
};
