#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
request(url + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const { characters } = JSON.parse(body);
    printInOrder(characters);
  }
});

async function printInOrder(characters) {
  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, _response, body) => {
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