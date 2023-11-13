#!/usr/bin/node
const x = Number(process.argv[2]);

if (Number.isInteger(x)) {
  let square = '';
  for (let i = 0; i < x - 1; i++) {
    square += 'X'.repeat(x) + '\n';
  }
  square += 'X'.repeat(x);
  console.log(square);
} else {
  console.log('Missing size');
}
