#!/usr/bin/node

const request = require('request');
const util = require('util');

// Convert request to use promises
const requestPromise = util.promisify(request);

// Base URL for Star Wars API
const BASE_URL = 'https://swapi.dev/api';

// Function to get character name from URL
async function getCharacterName (url) {
  try {
    const response = await requestPromise(url);
    const character = JSON.parse(response.body);
    return character.name;
  } catch (error) {
    console.error(`Error fetching character: ${error.message}`);
    return null;
  }
}

// Main function to get and print all characters
async function printMovieCharacters (movieId) {
  try {
    // Get movie data
    const movieUrl = `${BASE_URL}/films/${movieId}/`;
    const response = await requestPromise(movieUrl);
    const movie = JSON.parse(response.body);

    // Get all character names (maintaining order)
    const characterPromises = movie.characters.map(getCharacterName);
    const characters = await Promise.all(characterPromises);

    // Print character names (filtering out any null values from errors)
    characters.forEach(name => {
      if (name) console.log(name);
    });
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Get movie ID from command line argument
const movieId = process.argv[2];

// Validate movie ID
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

// Execute the main function
printMovieCharacters(movieId);
