#!/usr/bin/node
const request = require('request');

const Apiurl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
request(Apiurl + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const { characters } = JSON.parse(body);
    printInOrder(characters);
  }
});

async function printInOrder(characters) {
  characters.forEach(async (character) => {
    try {
      const characterBody = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(body);
          }
        });
      });
      console.log(JSON.parse(characterBody).name);
    } catch (error) {
      console.error('Error fetching character data:', error);
    }
  });
}
