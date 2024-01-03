#!/usr/bin/node

const writeFile = require('fs').writeFile;

const fileName = process.argv[2];
const string = process.argv[3];

writeFile(fileName, string, function () {
  console.log('SUCCESS');
});
