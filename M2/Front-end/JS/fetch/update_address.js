async function updateAddress(userID, data) {
  const url = `https://api.restful-api.dev/objects/${userID}`;

  const options = {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  const response = await fetch(url, options);
  if (response.ok) {
    return response.json();
  }
  throw new Error(`Could not update user id: ${userID}, ${response.status}`);
}

async function getUser(userID) {
  /*
    Had to created this function, and adapte all code, because restful-api, patch all data, so have to get it first and merge with new data
     */
  const url = `https://api.restful-api.dev/objects/${userID}`;
  const response = await fetch(url);

  if (response.ok) {
    return response.json();
  } else {
    throw new Error(`could not receive user id: ${userID}, ${response.status}`);
  }
}

try {
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
    formatData(user_data.data, "1949 Umoza Center")
  );
  console.log(user);
} catch (error) {
  console.error(error.message);
}
