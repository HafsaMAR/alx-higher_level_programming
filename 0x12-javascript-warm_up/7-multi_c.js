#!/usr/bin/node
const x = Number(process.argv[2]);

if (Number.isInteger(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
