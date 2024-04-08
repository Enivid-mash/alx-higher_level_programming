#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  } else if (n === 0 || n === 1) {
    return 1; // Factorial of 0 or 1 is 1
  } else {
    return n * factorial(n - 1); // Recursively compute factorial
  }
}

// Check if a command-line argument is provided
if (process.argv.length === 2) {
  console.log(1);
} else {
  // Parse the command-line argument to an integer
  const num = parseInt(process.argv[2]);

  // Compute factorial and display result
  const result = factorial(num);
  console.log(result);
}
