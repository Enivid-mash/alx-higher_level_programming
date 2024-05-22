#!/usr/bin/node

const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file content
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
