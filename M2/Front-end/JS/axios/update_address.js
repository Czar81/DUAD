const axios = require("axios");

async function updateAddress(userID, data) {
  const url = `https://api.restful-api.dev/objects/${userID}`;

  const response = await axios.patch(url, data);
  return response.data;
}

async function getUser(userID) {
  /*
    Had to created this function, and adapte all code, because restful-api, patch all data, so have to get it first and merge with new data
     */
  const url = `https://api.restful-api.dev/objects/${userID}`;
  const response = await axios.get(url);
  return response.data;
}

async function main() {
  const formatData = (currentData, newAddress) => ({
    data: {
      ...currentData,
      address: newAddress,
    },
  });
  const userID = "ff8081819782e69e019ba549354804ce";
  const user_data = await getUser(userID);
  const user = await updateAddress(
    userID,
    formatData(user_data.data, "1940 Umoza Center")
  );
  console.log(user);
}

main();
