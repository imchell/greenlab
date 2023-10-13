const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

let sequence = '';
let reading = false;

rl.on('line', (line) => {
  if (line.startsWith('>')) {
    reading = line.includes('THREE');
  } else if (reading) {
    sequence += line;
  }
});

rl.on('close', () => {
  sequence = sequence.toUpperCase();
  const counts = new Map();
  const lengths = [1, 2, 3, 4, 6, 12, 18];
  const sequences = ['GGT', 'GGTA', 'GGTATT', 'GGTATTTTAATT', 'GGTATTTTAATTTATAGT'];

  for (const length of lengths) {
    for (let i = 0; i <= sequence.length - length; i++) {
      const subseq = sequence.substr(i, length);
      counts.set(subseq, (counts.get(subseq) || 0) + 1);
    }
  }

  for (const length of [1, 2]) {
    const sorted = Array.from(counts.entries())
      .filter(([k, v]) => k.length === length)
      .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));

    let sum = sorted.reduce((acc, [k, v]) => acc + v, 0);
    for (const [k, v] of sorted) {
      console.log(`${k} ${((v / sum) * 100).toFixed(3)}`);
    }
    console.log();
  }

  for (const seq of sequences) {
    console.log(`${counts.get(seq) || 0}\t${seq}`);
  }
});