#!/usr/bin/node
function add (a, b) {
  const result = parseInt(process.argv[2]) + parseInt(process.argv[3]);
  console.log(result);
}

add();
