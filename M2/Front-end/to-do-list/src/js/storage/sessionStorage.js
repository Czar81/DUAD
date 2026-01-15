import { setCookie, getCookie, deleteCookie } from "../utils/cookie";

const UID_KEY = "uid";

export const setUserId = (id) => setCookie(UID_KEY, id);
export const getUserId = () => getCookie(UID_KEY);
export const clearUserId = () => deleteCookie(UID_KEY);
