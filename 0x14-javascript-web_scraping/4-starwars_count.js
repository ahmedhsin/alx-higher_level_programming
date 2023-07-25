#!/usr/bin/node

const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/';
const doLogic = (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  const personApi = 'https://swapi-api.alx-tools.com/api/people/18/';
  let cnt = 0;
  for (let i = 0; i < films.length; i++) {
    if (films[i].characters.includes(personApi)) cnt++;
  }
  console.log(cnt);
};

request(api, doLogic);
