export const popup = (typeInfo ,iconSrc, iconAlt, message) => {
const popup = document.createElement("div");
  popup.className = `popup ${typeInfo} visible`;
  const icon = document.createElement("img");
  icon.className = "popup-icon";
  icon.src = iconSrc;
  icon.alt = iconAlt;

  const title = document.createElement("p");
  title.className = "popup-title";
  title.textContent = message;

  const close = document.createElement("img");
  close.className = "popup-close";
  close.src = "/src/assets/icons/close.svg";
  close.alt="Close"

  close.addEventListener("click", () => {
    popup.remove();
  });

  popup.append(icon, title, close);
  document.body.appendChild(popup);

  setTimeout(() => {
    popup.remove();
  }, 5000);
}