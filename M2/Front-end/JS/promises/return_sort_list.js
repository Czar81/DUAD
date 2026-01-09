function resolveName(str, time_out) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(str);
    }, time_out);
  });
}

function capitalizeFirstLetter(val) {
  return val.charAt(0).toUpperCase() + val.slice(1);
}

const array = ["very", "dogs", "cute", "are"];
const index = [1, 3, 0, 2];
const promises = [];

for (let i of index) {
  promises.push(resolveName(array[i], 200));
}

Promise.all(promises).then((value) => {
  console.log(capitalizeFirstLetter(value.join(" ")));
});
