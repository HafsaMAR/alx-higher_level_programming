#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (_error, { statusCode }) {
  console.log(statusCode);
});
