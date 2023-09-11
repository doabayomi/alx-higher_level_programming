#!/usr/bin/node
const process = require('process');
const args = process.argv;
let validArgs = [];
let count = 0;
args.forEach((val, index) => {
  if (index > 1) {
    validArgs.push(Number(val));
  }
  count++
});

if (count === 2 || count === 3) {
  console.log(0);
} else {
  validArgs.sort();
  validArgs.reverse();
  console.log(validArgs[1]);
}
