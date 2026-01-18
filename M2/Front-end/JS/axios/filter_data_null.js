const axios = require("axios");

async function getObjects() {
  const url = "https://api.restful-api.dev/objects";
  const response = await axios(url);
  return response.data;
}

function formattedObjects(objects) {
  let formatted = "";
  for (let object of objects) {
    if (object.data === null) {
      continue;
    }
    const data = Object.entries(object.data)
      .map(([key, value]) => `${key}: ${value}`)
      .join(", ");
    formatted += object.name + " (" + data + ")\n";
  }
  return formatted;
}

async function main() {
  const objects = await getObjects();
  console.log(formattedObjects(objects));
}

main()