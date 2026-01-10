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
  }
}

const user = await getUser("ff8081819782e69e019ba549354804ce");
console.log(user);

await getUser("ff8081819782e69e019ba5493548041");
