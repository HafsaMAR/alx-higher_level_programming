#!/usr/bin/node

const { readFile } = require('fs');

const fileName = process.argv[2];

readFile(fileName, 'utf-8', (err, content) => {
  if (err) {
    console.error(err);
  }
  console.log(content);
});