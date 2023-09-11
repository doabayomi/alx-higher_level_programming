#!/usr/bin/node
const process = require('process');
const args = process.argv;
let count = 0;
args.forEach((val, index) => {
  count++;
});

if (count <= 2) {
  console.log('Missing number of occurrences');
} else {
  const noOfTimesToPrint = Number(args[2]);
  let timesPrinted = 0;
  while (timesPrinted < noOfTimesToPrint) {
    console.log('C is fun');
    timesPrinted++;
  }
}
