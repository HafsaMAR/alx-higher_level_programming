#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (_error, response, rawBody) {
  const body = JSON.parse(rawBody);
  const films = body.results;

  const characters = films.map(function (film) {
    return film.characters
      .map(
        function (url) {
          return url === 'https://swapi-api.alx-tools.com/api/people/18/';
        }
      )
      .filter(function (element) { return element; }).length;
  });

  console.log(
    characters.reduce(
      function (acc, curr) { return acc + curr; },
      0
    )
  );
});
