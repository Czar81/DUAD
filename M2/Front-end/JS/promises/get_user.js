function getUser(userId) {
  // With https://reqres.in/api/users/2 receive 403, I think from claudflare, not sure
  const url = `https://jsonplaceholder.typicode.com/users/${userId}`;
  return fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}

getUser(2);
