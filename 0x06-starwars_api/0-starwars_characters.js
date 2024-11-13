#!/usr/bin/node

const request = require('request');

// Check if the movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Error fetching movie data:', err);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', res.statusCode);
    process.exit(1);
  }

  // Get the characters URLs from the film data
  const characterUrls = body.characters;

  // Request each character's data and print their names
  characterUrls.forEach((characterUrl, index) => {
    request(characterUrl, { json: true }, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error('Error fetching character data:', charErr);
        process.exit(1);
      }

      if (charRes.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', charRes.statusCode);
        process.exit(1);
      }

      console.log(charBody.name);
    });
  });
});
