#!/usr/bin/node
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/', { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const actorurl = body.characters;
  actorurl.forEach(urls => {
    request(urls, { json: true }, (err, res, actorbody) => {
      if (err) {
        console.log(error);
      }
      console.log(actorbody.name);
    });
  });
});
