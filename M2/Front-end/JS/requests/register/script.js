async function createUser(data) {
    const url = "https://api.restful-api.dev/objects";
    const response = await axios.post(url, data);
    return response.data
}

function formatValues() {
    return {
        name: document.getElementById("name-user").value,
        data: {
            email: document.getElementById("email-user").value,
            address: document.getElementById("short-address").value,
            password: document.getElementById("password-user").value
        }
    };
}

function validatePass(pass1, pass2) {
    if (pass1 === pass2) {
        errorMsg.textContent = "";
        return true;
    } else {
        errorMsg.textContent = "Las contraseñas no coinciden";
        return false;
    }
}

async function main() {
    if (!validatePass(pass1Input.value, pass2Input.value)) {
        return;
    }
    try {
        btn_submit.disabled = true;
        const values = formatValues();
        const response = await createUser(values);
        document.cookie = `userID=${response.id}; path=/; SameSite=Lax; max-age=31536000`
        alert(`Usuario creado correctamente, tu id es: ${String(response.id)}`);
        setTimeout(() => {
    location.replace("../profile/my_profile.html");
}, 50);
    } catch (err) {
        console.error(err);
        errorMsg.textContent = "Error al crear el usuario";
    } finally {
        btn_submit.disabled = false;
    }
}

const form = document.getElementById("form-register")
const pass2Input = document.getElementById("password-confirm")
const pass1Input = document.getElementById("password-user")

const errorMsg = document.getElementById("errorMsg");
const btn_submit = document.getElementById("btn-register")


pass2Input.addEventListener("input", () => {
    validatePass(pass1Input.value, pass2Input.value)
});

form.addEventListener("submit", (event) => {
    event.preventDefault()
    main()
})
