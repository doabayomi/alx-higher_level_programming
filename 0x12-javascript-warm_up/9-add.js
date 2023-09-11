#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const process = require('process');
const args = process.argv;
const firstArgument = Number(args[2]);
const secondArgument = Number(args[3]);
console.log(add(firstArgument, secondArgument));
