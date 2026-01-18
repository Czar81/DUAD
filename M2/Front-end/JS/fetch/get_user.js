async function getUser(userID) {
  try {
    const url = `https://api.restful-api.dev/objects/${userID}`;
    const response = await fetch(url);

    if (response.ok) {
      return response.json();
    } else {
      throw new Error(
        `could not receive user id: ${userID}, ${response.status}`
      );
    }
  } catch (error) {
    console.error(`${error}`);
    return null
  }
}

const user_ok = await getUser("ff8081819782e69e019ba549354804ce");

const user_fal = await getUser("ff8081819782e69e019ba5493548041");

Promise.all([user_ok, user_fal]).then((value) => {
  console.log(value);
});

