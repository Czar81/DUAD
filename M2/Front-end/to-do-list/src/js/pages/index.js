import { checkSession } from "../services/authService.js"
import { getCookie } from "../utils/cookie.js"

export const initIndexPage = () => {
    const uid = getCookie("uid")
    if (!uid) {
        window.location.replace("/M2/Front-end/to-do-list/src/pages/signup.html")
    }
    const valid = checkSession(uid)
    if (!valid) {
        window.location.replace("/M2/Front-end/to-do-list/src/pages/login.html")
    }   
    window.location.replace("/M2/Front-end/to-do-list/src/pages/to-do.html")
}