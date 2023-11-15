#!/usr/bin/node
const { dict } = require('./101-data');
const occurences = {};
for (const userId in dict) {
  const occurence = dict[userId];
  if (occurences[occurence] === undefined) {
    occurences[occurence] = [userId];
  } else {
    occurences[occurence].push(userId);
  }
}
console.log(occurences);
