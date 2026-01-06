function mysplit(str, div) {
  let result = [];
  let start = 0;

  for (let i = 0; i < str.length; i++) {
    if (str[i] === div) {
        console.log(i)
      result.push(str.slice(start, i));
      start = i + 1;
    }
  }

  result.push(str.slice(start));

  return result;
}


const example = "This is a string!"
console.log(mysplit(example, " "))