#!/usr/bin/node

const myargs = process.argv.slice(2);
if (isNaN(myargs[0])) {
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(myargs[0]));
}