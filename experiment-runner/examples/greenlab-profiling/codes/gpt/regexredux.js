const fs = require('fs');
const readline = require('readline');

const sequences = [
  'agggtaaa|tttaccct',
  '[cgt]gggtaaa|tttaccc[acg]',
  'a[act]ggtaaa|tttacc[agt]t',
  'ag[act]gtaaa|tttac[agt]ct',
  'agg[act]taaa|ttta[agt]cct',
  'aggg[acg]aaa|ttt[cgt]ccct',
  'agggt[cgt]aa|tt[acg]accct',
  'agggta[cgt]a|t[acg]taccct',
  'agggtaa[cgt]|[acg]ttaccct',
];

const magicSequences = [
  { pattern: 'tHa[Nt]', replace: '<4>' },
  { pattern: 'aND|caN|Ha[DS]|WaS', replace: '<3>' },
  { pattern: 'a[NSt]|BY', replace: '<2>' },
  { pattern: '<[^>]*>', replace: '|' },
  { pattern: '\\|[^|][^|]*\\|', replace: '-' },
];

let sequence = '';
let sequenceLengths = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

rl.on('line', (line) => {
  if (!line.startsWith('>')) {
    sequence += line;
  }
});

rl.on('close', () => {
  sequenceLengths.push(sequence.length);

  sequences.forEach((seq) => {
    const regex = new RegExp(seq, 'g');
    const matches = sequence.match(regex);
    console.log(`${seq} ${matches ? matches.length : 0}`);
  });

  magicSequences.forEach(({ pattern, replace }) => {
    sequence = sequence.replace(new RegExp(pattern, 'g'), replace);
  });

  sequenceLengths.push(sequence.length);

  sequence = sequence.replace(/[^BDEFHIJKLMNOPQRSUVWXYZ]/g, '');
  sequenceLengths.push(sequence.length);

  console.log(sequenceLengths.join('\n'));
});
