#!/usr/bin/node
function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
};

console.log(factorial(Number(process.argv[2])));
