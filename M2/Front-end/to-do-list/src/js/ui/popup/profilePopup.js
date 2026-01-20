import { getUserFromState } from "@state/userState.js";
import { openProfileUser, closeProfileUser } from "@render/profileRender.js";

export const showPopupProfile = () => {
  const user = getUserFromState();
  openProfileUser(user);
};

export const closePopupProfile = () => {
  closeProfileUser();
};
