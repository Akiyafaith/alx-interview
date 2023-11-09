#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    await printInOrder(characters);
  }
});

async function printInOrder(characters) {
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
}
