#!/usr/bin/python3

import sys
import re

def main():
    # Read the entire input
    data = sys.stdin.read()

    # Record the initial sequence length
    initial_length = len(data)

    # Remove FASTA sequence descriptions and linefeed characters
    data = re.sub('>.*\n|\n', '', data)
    processed_length = len(data)

    # Patterns representing DNA 8-mers
    dna_patterns = [
        "agggtaaa|tttaccct",
        "[cgt]gggtaaa|tttaccc[acg]",
        "a[act]ggtaaa|tttacc[agt]t",
        "ag[act]gtaaa|tttac[agt]ct",
        "agg[act]taaa|ttta[agt]cct",
        "aggg[acg]aaa|ttt[cgt]ccct",
        "agggt[cgt]aa|tt[acg]accct",
        "agggta[cgt]a|t[acg]taccct",
        "agggtaa[cgt]|[acg]ttaccct"
    ]

    # Count matches for each pattern
    for pattern in dna_patterns:
        count = len(re.findall(pattern, data))
        print(pattern, count)

    # Magic patterns and their replacements
    magic_patterns = [
        ("tHa[Nt]", "<4>"),
        ("aND|caN|Ha[DS]|WaS", "<3>"),
        ("a[NSt]|BY", "<2>"),
        ("<[^>]*>", "|"),
        ("\\|[^|][^|]*\\|", "-")
    ]

    # Match and replace for each magic pattern
    for pattern, replacement in magic_patterns:
        data = re.sub(pattern, replacement, data)
    magic_processed_length = len(data)

    # Print the 3 recorded sequence lengths
    print()
    print(initial_length)
    print(processed_length)
    print(magic_processed_length)

if __name__ == "__main__":
    main()
