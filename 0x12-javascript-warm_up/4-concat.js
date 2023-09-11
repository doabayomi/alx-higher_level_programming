#!/usr/bin/node
const process = require('process');
const args = process.argv;

const subjectWord = args[2];
const objectWord = args[3];
console.log(subjectWord + ' is ' + objectWord);
