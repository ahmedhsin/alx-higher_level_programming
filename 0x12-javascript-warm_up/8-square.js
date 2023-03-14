#!/usr/bin/node

const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let line = '';
  for (let j = 0; j < num; j++) {
    line = line + 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}
