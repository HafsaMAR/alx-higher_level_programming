#!/usr/bin/node

const request = require('request');
const { writeFile } = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, _response, body) {
  if (error) {
    console.log(error);
    return;
  }

  writeFile(path, body, () => {})
});
