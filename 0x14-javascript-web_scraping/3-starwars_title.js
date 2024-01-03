#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (_error, { response }, body) {
  const result = JSON.parse(body);

  console.log(result.title);
});
