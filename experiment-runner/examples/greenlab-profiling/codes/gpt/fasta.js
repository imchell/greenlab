const IM = 139968;
const IA = 3877;
const IC = 29573;
let LAST = 42;

const ALU =
  "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGATCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAA";

const IUB = [
  ["a", 0.27],
  ["c", 0.12],
  ["g", 0.12],
  ["t", 0.27],
  ["B", 0.02],
  ["D", 0.02],
  ["H", 0.02],
  ["K", 0.02],
  ["M", 0.02],
  ["N", 0.02],
  ["R", 0.02],
  ["S", 0.02],
  ["V", 0.02],
  ["W", 0.02],
  ["Y", 0.02],
];

const HomoSapiens = [
  ["a", 0.3029549426680],
  ["c", 0.1979883004921],
  ["g", 0.1975473066391],
  ["t", 0.3015094502008],
];

function toCumulative(arr) {
  let cumul = 0.0;
  for (let i = 0; i < arr.length; i++) {
    cumul += arr[i][1];
    arr[i][1] = cumul;
  }
}

function fastaRandom(n, arr) {
  toCumulative(arr);
  let ret = "";
  for (let i = 0; i < n; i++) {
    let r = genRandom();
    for (let j = 0; j < arr.length; j++) {
      if (r < arr[j][1]) {
        ret += arr[j][0];
        break;
      }
    }
    if (ret.length >= 60) {
      console.log(ret.substring(0, 60));
      ret = ret.substring(60);
    }
  }
  if (ret.length > 0) console.log(ret);
}

function fastaRepeat(n, seq) {
  let ret = "";
  let seqi = 0;
  for (let i = 0; i < n; i++) {
    ret += seq[seqi];
    seqi++;
    if (seqi == seq.length) seqi = 0;
    if (ret.length >= 60) {
      console.log(ret.substring(0, 60));
      ret = ret.substring(60);
    }
  }
  if (ret.length > 0) console.log(ret);
}

function genRandom(max = 1) {
  LAST = (LAST * IA + IC) % IM;
  return (max * LAST) / IM;
}

function main(n) {
  console.log(">ONE Homo sapiens alu");
  fastaRepeat(n * 2, ALU);
  console.log(">TWO IUB ambiguity codes");
  fastaRandom(n * 3, IUB);
  console.log(">THREE Homo sapiens frequency");
  fastaRandom(n * 5, HomoSapiens);
}

main(1000);