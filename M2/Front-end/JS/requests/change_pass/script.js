async function getUser(userID) {
  /*
    Had to created this function, and adapte all code, because restful-api, patch all data, so have to get it first and merge with new data
     */
  const url = `https://api.restful-api.dev/objects/${userID}`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(error);
    return false;
  }
}

async function updatePass(userID, data) {
  const url = `https://api.restful-api.dev/objects/${userID}`;
  try {
    await axios.patch(url, data);
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
}

function validatePass(pass1, pass2) {
  if (pass1 === pass2) {
    return true;
  } else {
    return false;
  }
}

async function main() {
  try {
    btn_submit.disabled = true;
    if (!validatePass(passNew.value, passConfirm.value)) {
      errorMsg.textContent = "Las contraseñas nuevas no coinciden";
      return;
    }
    console.log("id", userID.value);
    const user = await getUser(userID.value);
    if (!user) {
      errorMsg.textContent = "Usuario no encontrado";
      return;
    }
    if (!validatePass(passOld.value, String(user.data.password))) {
      errorMsg.textContent = "Las contraseña antiguas no coinciden";
      return;
    }
    const updated = await updatePass(
      user.id,
      formatData(user.data, passNew.value)
    );
    if (updated) {
      errorMsg.textContent = "";
      alert("Contraseña actualizada con éxito");
      form.reset();
    } else {
      errorMsg.textContent = "Error al actualizar la contraseña";
    }
  } catch (error) {
    console.error(error);
    return;
  } finally {
    btn_submit.disabled = false;
  }
}

const formatData = (currentData, newPass) => ({
  data: {
    ...currentData,
    password: newPass,
  },
});

const form = document.getElementById("form-change-pass");
const userID = document.getElementById("user-id");
const passOld = document.getElementById("old-password");
const passNew = document.getElementById("new-password");
const passConfirm = document.getElementById("password-confirm");

const errorMsg = document.getElementById("errorMsg");
const btn_submit = document.getElementById("btn-change");

passConfirm.addEventListener("input", () => {
  if (!validatePass(passNew.value, passConfirm.value)) {
    errorMsg.textContent = "Las contraseñas nuevas no coinciden";
  } else {
    errorMsg.textContent = "";
  }
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  main();
});
