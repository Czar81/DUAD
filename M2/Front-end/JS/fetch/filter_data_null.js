async function getObjects() {
  const url = "https://api.restful-api.dev/objects";
  const response = await fetch(url);
  return response.json();
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

const objects = await getObjects();
console.log(formattedObjects(objects));
