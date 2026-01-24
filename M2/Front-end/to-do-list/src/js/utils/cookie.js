export const setCookie = (name, value, options) =>
  (document.cookie = `${name}=${value}; path=/; ${options}`);

export const getCookie = (name) =>
  document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)")?.pop() || "";

export const deleteCookie = (name) =>
  (document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`);
