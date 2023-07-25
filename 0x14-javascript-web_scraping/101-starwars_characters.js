#!/usr/bin/node

const request = require('request-promise');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const getName = async (url) => {
  const body = await request(url);
  const person = JSON.parse(body);
  console.log(person.name);
};
const doLogic = async () => {
  const body = await request(api);
  const films = JSON.parse(body).results;
  const movieChars = films[parseInt(process.argv[2]) - 1].characters;
  for (let i = 0; i < movieChars.length; i++) {
    await getName(movieChars[i]);
  }
};
doLogic();
