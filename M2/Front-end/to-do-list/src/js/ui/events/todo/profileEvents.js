import { showPopupProfile, closePopupProfile } from "@popup/profilePopup.js";

export const bindProfileEvents = () => {
  const profile = document.getElementById("name-img");
  profile.addEventListener("click", () => {
    showPopupProfile();
  });
  const btnClose = document.querySelector(".close-btn");
  btnClose.addEventListener("click", () => {
    closePopupProfile();
  });
};
