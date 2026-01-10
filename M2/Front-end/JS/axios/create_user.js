const axios = require("axios");

async function createUser(name, email, password, address) {
  const data = {
    name: name,
    data: {
      email: email,
      password: password,
      address: address,
    },
  };

  const url = "https://api.restful-api.dev/objects";
  const response = await axios.post(url, data);
  return response.data
}

try {
  createUser(
    "jonh",
    "jonhdoe@example.com",
    "secret_password",
    "501 Satnaj Court"
  ).then((user)=> console.log(user));

} catch (error) {
  console.error(error.message);
}
