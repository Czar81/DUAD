let userState = {};

export const setUserState = (user) => {
  userState = user;
};

export const removeTaskFromState = () => {
  userState = {};
};

export const getUserFromState = () => userState;
