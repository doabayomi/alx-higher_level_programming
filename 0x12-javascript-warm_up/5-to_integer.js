#!/usr/bin/node
const process = require('process');
const args = process.argv;

const inputNumber = Number(args[2]);
if (isNaN(inputNumber) || inputNumber === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + inputNumber);
}
