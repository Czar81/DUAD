async function getUser(userId) {
  // With https://reqres.in/api/users/2 receive 403, I think from claudflare, not sure
  const url = `https://jsonplaceholder.typicode.com/users/${userId}`;
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.log(`Error happened ${err}`);
  }
}

const user_info = getUser(2);
