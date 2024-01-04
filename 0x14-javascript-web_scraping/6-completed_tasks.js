#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, _response, rawBody) => {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = JSON.parse(rawBody);

  const result = {};

  for (const task of tasks) {
    const id = task.userId;

    if (task.completed) {
      result[id] = (result[id] ?? 0) + 1;
    }
  }

  console.log(result);
});
