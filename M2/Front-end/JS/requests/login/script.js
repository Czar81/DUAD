async function getUser(userID) {
  const url = `https://api.restful-api.dev/objects/${userID}`;
  const response = await axios.get(url);
  return response.data;
}

function validatePass(pass1, pass2) {
  console.log(pass1, pass2);
  if (pass1 === pass2) {
    errorMsg.textContent = "";
    return true;
  } else {
    errorMsg.textContent = "El ID o la contraseña son incorrectas";
    return false;
  }
}

async function main() {
  try {
    btn_submit.disabled = true;
    const userID = document.getElementById("user-id").value;
    const user = await getUser(userID);
    if (!validatePass(passInput.value, user.data.password)) {
      return;
    }
    document.cookie = `userID=${user.id}; path=/; SameSite=Lax; max-age=31536000`;
    alert(`Sesion iniciada correctamente, tu id es: ${String(user.id)}`);
    setTimeout(() => {
      location.replace("../profile/my_profile.html");
    }, 10);
  } catch (err) {
    console.error(err);
    errorMsg.textContent = "Error al iniciar sesion";
  } finally {
    btn_submit.disabled = false;
  }
}

const form = document.getElementById("form-login");
const passInput = document.getElementById("password-user");

const errorMsg = document.getElementById("errorMsg");
const btn_submit = document.getElementById("btn-login");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  main();
});
