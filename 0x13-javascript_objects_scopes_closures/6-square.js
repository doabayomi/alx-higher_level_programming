#!/usr/bin/node
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string = string + c;
      }
      console.log(string);
    }
  }
};
