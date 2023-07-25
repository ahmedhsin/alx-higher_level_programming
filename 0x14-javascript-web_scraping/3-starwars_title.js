#!/usr/bin/node

const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(api, (err, res, body) => {
  if (err) console.log(err);
  const json = JSON.parse(body);
  console.log(json.title);
});
