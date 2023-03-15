#!/usr/bin/node
exports.esrever = function (list) {
  if (list === undefined) { return undefined; }
  const length = list.length;
  for (let i = 0; i < length / 2; i++) {
    const tmp = list[i];
    list[i] = list[length - 1 - i];
    list[length - 1 - i] = tmp;
  }
  return list;
};
