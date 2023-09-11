#!/usr/bin/node
const process = require('process');
const args = process.argv;
let count = 0;
args.forEach((val, index) => {
  count++;
});

if (count <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
