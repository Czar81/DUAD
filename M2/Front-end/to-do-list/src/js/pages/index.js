import { checkSession } from "../services/authService.js"
import { getCookie } from "../utils/cookie.js"

export const initIndexPage = async () => {
    const uid = getCookie("uid")
    if (!uid) {
        return window.location.replace("/M2/Front-end/to-do-list/src/pages/signup.html")
    }
    const valid = await checkSession(uid)
    if (!valid) {
        return window.location.replace("/M2/Front-end/to-do-list/src/pages/login.html")
    }
    window.location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html")
}