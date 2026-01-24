export const openProfileUser = (user) => {
  const cardInfo = document.querySelector(".card-info");
  const lastName = document.getElementById("last-name-card");
  const name = document.getElementById("name-card");
  const id = document.getElementById("info-id");
  const email = document.getElementById("info-email");
  name.textContent = user.name;
  id.textContent = user.id;
  email.textContent = user.data.email;
  cardInfo.style.display = "flex";
  lastName.textContent = user.data.lastname;
};

export const closeProfileUser = () => {
  const cardInfo = document.querySelector(".card-info");

  cardInfo.style.display = "none";
};
