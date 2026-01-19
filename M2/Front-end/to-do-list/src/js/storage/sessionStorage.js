import { setCookie, getCookie, deleteCookie } from "@utils/cookie.js";

const UID_KEY = "uid";

export const setUserId = (id) => setCookie(UID_KEY, id, "max-age=31536000");
export const getUserId = () => getCookie(UID_KEY);
export const clearUserId = () => deleteCookie(UID_KEY);
