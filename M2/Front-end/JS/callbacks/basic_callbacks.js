function evalueted(num, evenFunc, oddFunc) {
  if (num % 2 == 0) {
    evenFunc();
  } else {
    oddFunc();
  }
}

const evenFunc = () => console.log("The Number is even!");
const oddFunc  = () => console.log("The Number is odd!");

evalueted(22, evenFunc, oddFunc);
