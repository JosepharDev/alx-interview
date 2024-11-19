#!/usr/bin/node
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/', { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const actorUrls = body.characters;
  const actorPromises = actorUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, { json: true }, (err, res, actorBody) => {
        if (err) {
          reject(err);
        } else {
          resolve(actorBody.name); // Resolve with actor's name
        }
      });
    });
  });
  Promise.all(actorPromises)
    .then(actorNames => {
      actorNames.forEach(name => {
        console.log(name); // Print each name in order
      });
    })
    .catch(error => {
      console.error(error); // Print any errors that occur
    });
});
