#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, _response, rawBody) {
  if (error) {
    console.log(error);
    return;
  }
  const body = JSON.parse(rawBody);
  const films = body.results;

  let count = 0;
  for (const film of films) {
    const characters = film.characters;

    for (const character of characters) {
      if (character.match(/18/g)) {
        count++;
      }
    }
  }
  console.log(count);
});
