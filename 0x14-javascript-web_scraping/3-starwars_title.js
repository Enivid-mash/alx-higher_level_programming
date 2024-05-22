#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first argument
const movieId = parseInt(process.argv[2], 10);

// Endpoint URL for the Star Wars API
const endpointUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(endpointUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      // Parse the response body as JSON
      const movie = JSON.parse(body);

      // Print the movie title
      console.log(`${movie.title}`);
    } catch (err) {
      console.error(err);
    }
  }
});
