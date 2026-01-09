function getUser(userId) {
  // With https://reqres.in/api/users/2 receive 403, I think from claudflare, not sure
  const url = `https://jsonplaceholder.typicode.com/users/${userId}`;
  return fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((err) => {
      console.error(`Error happened ${err}`);
    });
}

getUser(23);
