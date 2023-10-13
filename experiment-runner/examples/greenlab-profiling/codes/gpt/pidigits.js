const bigInt = require("big-integer");

let i = 0, k = 0, k2 = 1;
let acc = bigInt(0);
let den = bigInt(1);
let num = bigInt(1);
let ns = 0;

const n = process.argv[2] ? parseInt(process.argv[2]) : 10000;

while (i < n) {
  k++;
  k2 += 2;

  acc = acc.plus(num.times(2)).times(k2);
  den = den.times(k2);
  num = num.times(k);

  if (num.gt(acc)) {
    continue;
  }

  let tmp = num.times(3).plus(acc);
  let d3 = tmp.divide(den);
  
  tmp = tmp.plus(num);
  let d4 = tmp.divide(den);
  
  if (!d3.equals(d4)) {
    continue;
  }

  const d = d3.toJSNumber();
  ns = ns * 10 + d;
  i++;
  let last = i >= n;
  if (i % 10 == 0 || last) {
    console.log(pad(ns, last) + '\t:' + i);    
    ns = 0;
  }

  if (last) break;

  acc = acc.minus(den.times(d)).times(10);
  num = num.times(10);
}

function pad(i, last) {
  let res = i.toString();
  let count = 10 - res.length;
  while (count > 0) {
    last ? res += ' ' : res = '0' + res;
    count--;
  }
  return res;
}