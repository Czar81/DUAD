const axios = require("axios");

async function getUser(userID) {
  try {
    const url = `https://api.restful-api.dev/objects/${userID}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(`Error with user id: ${userID} ${error.message}`);
    return null;
  }
}

async function main() {
  const user_ok = await getUser("ff8081819782e69e019ba549354804ce");
  console.log(user_ok)
  await getUser("ff8081819782e69e019ba5493548041");
}
