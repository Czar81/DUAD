async function getUser(userID) {
  const url = `https://api.restful-api.dev/objects/${userID}`;
  const response = await axios.get(url);
  return response.data;
}

function validateSession(userID, user_db) {
  return String(user_db) === userID;
}

function closeSession() {
  document.cookie = `userID=; path=/; SameSite=Lax; expires=Thu, 01 Jan 1970 00:00:00 UTC`;
  alert("Sesion cerrada, hasta luego");
  setTimeout(() => {
    location.replace("../login/login.html");
  }, 5);
}

function showUserData(user) {
  const card = document.getElementById("profile-cards");
  card.innerHTML = `
        <h3>${user.name}</h3>
        <p><strong>ID:</strong> ${user.id}</p>
        <p><strong>Email:</strong> ${user.data.email}</p>
        <p><strong>Dirección:</strong> ${user.data.address}</p>
    `;
}

const getCookieValue = (name) =>
  document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)")?.pop() || "";

async function main() {
  try {
    const userID = getCookieValue("userID");
    if (!userID) {
      location.replace("../login/login.html");
      return;
    }
    const user_db = await getUser(userID);
    const isValid = validateSession(userID, user_db.id);

    if (!isValid) {
      location.replace("../login/login.html");
      return;
    }
    const btn_close = document.getElementById("btn-quick");
    showUserData(user_db);
    btn_close.addEventListener("click", closeSession);
  } catch (err) {
    console.error(err);
  }
}

main();
