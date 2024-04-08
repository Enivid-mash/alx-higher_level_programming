#!/usr/bin/node
let result = '';
if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < process.argv[2]; i++) {
    result += 'x';
  }
} else {
  console.log('Missing size');
}
for (let j = 0; j < process.argv[2]; j++) {
  console.log(result);
}
