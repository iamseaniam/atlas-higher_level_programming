#!/usr/bin/node

const c_fun = 'C is fun'

if (process.argv[2] && !isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(c_fun);
  }
  process.exit();
} else {
  console.log('Missing number of occurrences');
}
