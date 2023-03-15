#!/usr/bin/node
const min = (a, b) => {
  if (a > b) { return b; }
  return a;
};
module.exports = class Rectangle {
  constructor (w, h) {
    if (w !== undefined && h !== undefined && min(w, h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) { row += 'X'; }
    for (let i = 0; i < this.height; i++) { console.log(row); }
  }
};
