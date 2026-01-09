const nums = [
  3, 7, 12, 18, 25, 31, 42, 56, 63, 74, 81, 95, 104, 117, 129, 142, 158, 171,
  186, 199,
];

let even_num = [];

// Even numbes with for
for (const num of nums) {
  if (num % 2 === 0) {
    even_num.push(num);
  }
}
// Log of for
console.log(even_num);

// Even numbes with filter
even_num = nums.filter(num => num % 2 === 0);

// Log of filter
console.log(even_num);
