const fs = require("fs");
const path = require("path");

function readFileSync(file_name) {
  const filePath = path.join(__dirname, file_name);
  const data = fs.readFileSync(filePath, "utf8");
  return data.split("\r\n");
}

const file1 = readFileSync("file1.txt");
const file2 = readFileSync("file2.txt");
const compareFile = (file1, file2)=>{
    const set2 = new Set(file2)
    return file1.filter(item => set2.has(item))
}

console.log(compareFile(file1, file2));