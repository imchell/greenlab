#!/usr/bin/python3

import sys

def reverse_complement(sequence):
    # Define the complement mapping
    complement = {
        'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 
        'M': 'K', 'R': 'Y', 'W': 'W', 'S': 'S', 
        'Y': 'R', 'K': 'M', 'V': 'B', 'H': 'D', 
        'D': 'H', 'B': 'V', 'N': 'N',
        'a': 'T', 'c': 'G', 'g': 'C', 't': 'A', 
        'm': 'K', 'r': 'Y', 'w': 'W', 's': 'S', 
        'y': 'R', 'k': 'M', 'v': 'B', 'h': 'D', 
        'd': 'H', 'b': 'V', 'n': 'N'
    }
    
    # Use a generator expression to get the complement and then join the results into a string
    # Also, reverse the string using [::-1]
    return ''.join(complement[base] for base in sequence[::-1])

def main():
    # Initialize an empty list to store sequences
    sequences = []
    
    # Iterate over each line in stdin
    for line in sys.stdin:
        # If the line starts with '>', it's a descriptor
        if line.startswith('>'):
            # If we already have sequences, yield them, then clear the list
            if sequences:
                yield ''.join(sequences)
                sequences.clear()
            yield line.strip()
        else:
            # Otherwise, it's a sequence line, so append it to our list
            sequences.append(line.strip())

    # Yield the last sequence, if there is one
    if sequences:
        yield ''.join(sequences)

if __name__ == "__main__":
    # For each sequence, print its reverse complement
    for line in main():
        if line.startswith('>'):
            print(line)
        else:
            print(reverse_complement(line))

