#!/usr/bin/node
const fs = require('fs');

const firstSourceFile = process.argv[2];
const secondSourceFile = process.argv[3];
const destinationFile = process.argv[4];

const contentFirstFile = fs.readFileSync(firstSourceFile, 'utf8');
const contentSecondFile = fs.readFileSync(secondSourceFile, 'utf8');

fs.writeFileSync(destinationFile, contentFirstFile + contentSecondFile);
