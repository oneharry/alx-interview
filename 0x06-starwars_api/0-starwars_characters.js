#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  printChars(chars, 0);
});

const printChars = (chars, num) => {
  if (num === chars.length) {
    return;
  }
  request(chars[num], (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printChars(chars, num + 1);
  });
};
