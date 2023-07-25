#!/usr/bin/node

const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/';
const getName = (url) => {
  request(url, (err, res, body) => {
    if (err) console.log(err);
    const person = JSON.parse(body);
    console.log(person.name);
  });
};
const doLogic = (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  const movieChars = films[parseInt(process.argv[2]) - 1].characters;
  for (let i = 0; i < movieChars.length; i++) {
    getName(movieChars[i]);
  }
};

request(api, doLogic);
