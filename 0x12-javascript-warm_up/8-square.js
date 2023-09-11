#!/usr/bin/node
const process = require('process');
const args = process.argv;

const sizeOfSquare = Number(args[2]);
if (sizeOfSquare === undefined || isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeOfSquare; i++) {
    let string = '';
    for (let j = 0; j < sizeOfSquare; j++) {
      string = string + 'X';
    }
    console.log(string);
  }
}
