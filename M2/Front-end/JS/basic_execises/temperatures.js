const celsius = [-2, 0, 5, 9, 13, 18, 22, 27, 31, 36];

const fahrenheit = celsius.map(temperature => Math.round(temperature*1.8+32));

console.log(fahrenheit)