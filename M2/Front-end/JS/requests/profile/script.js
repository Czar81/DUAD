async function getUser(userID) {
    const url = `https://api.restful-api.dev/objects/${userID}`;
    const response = await axios.get(url);
    return response.data
}

async function validateSesion(getCookieValue) {
    const userID = getCookieValue("userID")
    if (!userID) {
        throw new Error("Unauthorized, redirecting to login")
    }
    try {
        const response = await getUser(userID)
        if(String(response.id)===userID){
            return true
        }
    } catch (err) {
        
    }
    
}

const getCookieValue = (name) => (
    document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
)

async function main() {
    try {
        if (!validateSesion(getCookieValue)) {
            location.replace("../login/login.html");
        }
        alert("logged")
    } catch (err) {
        console.error(err);
    }
}

main()
