async function createUser(name, email, password, address) {
  try {
    const data = {
      name: name,
      data: {
        email: email,
        password: password,
        address: address,
      },
    };
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    const url = "https://api.restful-api.dev/objects";
    const response = await fetch(url, options);

    if (response.ok) {
      return response.json();
    } else {
      throw new Error(
        `could not receive user id: ${userID}, ${response.status}`
      );
    }
  } catch (error) {
    console.error(`${error}`);
  }
}

const user = await createUser(
  "jonh",
  "jonhdoe@example.com",
  "secret_password",
  "501 Satnaj Court"
);
console.log(user);
