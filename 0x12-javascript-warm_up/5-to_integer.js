#!/usr/bin/node
if (process.argv.length > 2 && Number.isInteger(Number(process.argv[2]))) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
