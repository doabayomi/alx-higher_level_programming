#!/usr/bin/node
let lineCount = 0;
exports.logMe = function (item) {
  console.log(lineCount + ': ' + item);
  lineCount++;
};
