#!/usr/bin/node

const arr = [];
for (let i = 2; process.argv[i] !== undefined; i++) {
  arr.push(Number(process.argv[i]));
}
function kth (n, s, e) {
  const pivot = somelogic(s, e);
  if (pivot === n || s === e) { return arr[pivot]; } else if (pivot < n) { return kth(n, pivot + 1, e); } else { return kth(n, s, pivot - 1); }
}
function somelogic (s, e) {
  let l = s + 1;
  let r = e;
  while (l <= r) {
    if (arr[r] > arr[s]) { r--; } else {
      const tmp = arr[r];
      arr[r] = arr[l];
      arr[l] = tmp;
      l++;
    }
  }
  const tmp = arr[s];
  arr[s] = arr[r];
  arr[r] = tmp;
  return r;
}
if (arr.length <= 1) { console.log(0); } else { console.log(kth(arr.length - 2, 0, arr.length - 1)); }
