export const changeBtnState = (containerFilters, btnClick) => {
  containerFilters.querySelectorAll("button").forEach((button) => {
    button.classList.remove("btn-active");
    button.disabled = false;
  });
  btnClick.classList.add("btn-active");
  btnClick.disabled = true;
};
