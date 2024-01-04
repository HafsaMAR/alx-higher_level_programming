#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (_error, response, rawBody) {
  const body = JSON.parse(rawBody);
  const films = body.results;

  let count = 0;
  for (const film of films) {
    const characters = film.characters;

    for (const character of characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }

  console.log(count);
});
