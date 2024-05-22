#!/usr/bin/node

const request = require('request');
const apiEndpoint = process.argv[2];
const wedgeId = '18';
let wedgeMovieCount = 0;

request.get(apiEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const apiData = JSON.parse(body);
    apiData.results.forEach((movie) => {
      movie.characters.forEach((charUrl) => {
        if (charUrl.includes(wedgeId)) {
          wedgeMovieCount += 1;
        }
      });
    });
    console.log(wedgeMovieCount);
  }
});
