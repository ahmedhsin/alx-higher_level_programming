#!/usr/bin/node
function reverseStr (str) {
  str = str.split('');
  str = str.reverse();
  str = str.join('');
  return str;
}
exports.converter = function (base) {
  return (num) => {
    let answer = '';
    while (num > 0) {
      if (num % base < 10) {
        answer += num % base;
      } else {
        answer += String.fromCharCode(87 + (num % base));
      }
      num = Math.floor(num / base);
    }
    return reverseStr(answer);
  };
};
