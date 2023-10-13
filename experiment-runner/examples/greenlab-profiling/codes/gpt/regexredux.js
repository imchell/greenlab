const fs = require('fs');

function processInput(input) {
  const patterns = [
    /agggtaaa|tttaccct/g,
    /[cgt]gggtaaa|tttaccc[acg]/g,
    /a[act]ggtaaa|tttacc[agt]t/g,
    /ag[act]gtaaa|tttac[agt]ct/g,
    /agg[act]taaa|ttta[agt]cct/g,
    /aggg[acg]aaa|ttt[cgt]ccct/g,
    /agggt[cgt]aa|tt[acg]accct/g,
    /agggta[cgt]a|t[acg]taccct/g,
    /agggtaa[cgt]|[acg]ttaccct/g
  ];

  const magicPatterns = [
    /tHa[Nt]/g,
    /aND|caN|Ha[DS]|WaS/g,
    /a[NSt]|BY/g,
    /<[^>]*>/g,
    /\|[^|][^|]*\|/g
  ];

  let sequenceLengths = Array(patterns.length).fill(0);
  let sequence = input;

  for (let i = 0; i < patterns.length; i++) {
    const pattern = patterns[i];
    const matches = sequence.match(pattern);
    if (matches) {
      sequenceLengths[i] = matches.length;
    }
  }

  for (let i = 0; i < magicPatterns.length; i++) {
    sequence = sequence.replace(magicPatterns[i], `<${i + 2}>`);
  }

  const sequenceLengthString = sequenceLengths.join('\n');
  const output = sequenceLengths
    .map((count, index) => `${patterns[index].source} ${count}`)
    .join('\n') + '\n\n' + sequenceLengthString;

  return output;
}

const input = fs.readFileSync('input.txt', 'utf-8');
const output = processInput(input);
console.log(output);
