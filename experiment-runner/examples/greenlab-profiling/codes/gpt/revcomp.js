const readline = require('readline');

// Function to calculate the reverse complement of a DNA sequence
function reverseComplement(sequence) {
  const complementTable = {
    A: 'T',
    C: 'G',
    G: 'C',
    T: 'A',
    M: 'K',
    R: 'Y',
    W: 'W',
    S: 'S',
    Y: 'R',
    K: 'M',
    V: 'B',
    H: 'D',
    D: 'H',
    B: 'V',
    N: 'N'
  };

  return sequence
    .split('')
    .reverse()
    .map(base => complementTable[base] || base)
    .join('');
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

let currentSequence = null;

rl.on('line', line => {
  if (line.startsWith('>')) {
    if (currentSequence) {
      const reverseComp = reverseComplement(currentSequence);
      console.log(`${currentSequenceId} ${currentSequenceDesc}`);
      console.log(reverseComp);
    }

    // Extract ID and description from the header line
    const [, id, desc] = line.match(/^>(\S+)\s*(.*)/);

    // Initialize a new sequence
    currentSequenceId = id;
    currentSequenceDesc = desc;
    currentSequence = '';
  } else {
    // Append the sequence line
    currentSequence += line.trim();
  }
});

rl.on('close', () => {
  if (currentSequence) {
    const reverseComp = reverseComplement(currentSequence);
    console.log(`${currentSequenceId} ${currentSequenceDesc}`);
    console.log(reverseComp);
  }
});
