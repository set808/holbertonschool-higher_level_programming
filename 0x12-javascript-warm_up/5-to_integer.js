#!/usr/bin/node
/* Prints string */
'use strict';
const arg1 = process.argv[2];
const integer = parseInt(arg1, 10);
if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number:', integer);
}
