#!/usr/bin/node
const list = require('./100-data').list;
newlist = list.map((element, index, list) => element * index);
console.log(list)
console.log(newlist);

