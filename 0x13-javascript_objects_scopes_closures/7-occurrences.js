#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nocurrent = 0;
  if (list === undefined || searchElement === undefined) { return nocurrent; }
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { nocurrent += 1; }
  }
  return nocurrent;
};
