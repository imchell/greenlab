const readline = require('readline');

// Helper function to calculate the reverse complement of a DNA sequence
function reverseComplement(sequence) {
  const complementMap = {
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
    N: 'N',
  };

  return sequence.split('').reverse().map(base => complementMap[base] || base).join('');
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

let currentSequence = null;

rl.on('line', (line) => {
  if (line.startsWith('>')) {
    // Output the previous sequence's reverse complement (if exists)
    if (currentSequence) {
      const reverseComp = reverseComplement(currentSequence);
      console.log(`${currentSequence.id} ${currentSequence.description}\n${reverseComp}`);
    }

    // Parse sequence ID and description
    const [id, description] = line.substring(1).split(' ');
    currentSequence = {
      id,
      description,
      sequence: '',
    };
  } else {
    // Concatenate the sequence
    currentSequence.sequence += line.trim();
  }
});

rl.on('close', () => {
  // Output the reverse complement for the last sequence
  if (currentSequence) {
    const reverseComp = reverseComplement(currentSequence.sequence);
    console.log(`${currentSequence.id} ${currentSequence.description}\n${reverseComp}`);
  }
});
