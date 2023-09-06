#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const filmCharacters = data.characters;

  function fetchCharNames (index) {
    if (index < filmCharacters.length) {
      request(filmCharacters[index], (error, response, body) => {
        if (error) {
          console.error('Request error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Request failed with status code:', response.statusCode);
          return;
        }

        const data = JSON.parse(body);
        const characterName = data.name;
        console.log(characterName);
        fetchCharNames(index + 1);
      });
    }
  }
  fetchCharNames(0);
});
