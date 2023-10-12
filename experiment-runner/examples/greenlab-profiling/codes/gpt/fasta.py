# import argparse
# import random

# # Constants for linear congruential generator
# IM = 139968
# IA = 3877
# IC = 29573
# Seed = 42

# def random_number(max_value):
#     global Seed
#     Seed = (Seed * IA + IC) % IM
#     return max_value * Seed / IM

# def generate_dna_sequence_copy(source_sequence, length):
#     sequence = ""
#     source_length = len(source_sequence)
#     for _ in range(length):
#         index = random.randint(0, source_length - 1)
#         sequence += source_sequence[index]
#     return sequence

# def generate_dna_sequence_weighted(alphabet1, alphabet2, probabilities, length):
#     cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
#     sequence = ""
#     for _ in range(length):
#         rand_num = random_number(1.0)
#         for i, cum_prob in enumerate(cumulative_probabilities):
#             if rand_num <= cum_prob:
#                 sequence += alphabet1[i] if i < len(alphabet1) else alphabet2[i - len(alphabet1)]
#                 break
#     return sequence

# def main():
#     parser = argparse.ArgumentParser(description="Generate DNA sequences")
#     parser.add_argument("length", type=int, help="Length of the DNA sequence")
#     args = parser.parse_args()

#     # Example usage
#     source_sequence = "AGCT"
#     length = args.length
#     alphabet1 = "AC"
#     alphabet2 = "GT"
#     probabilities = [0.3, 0.2]  # Adjust these probabilities as needed

#     dna_sequence_copy = generate_dna_sequence_copy(source_sequence, length)
#     print("DNA Sequence (Copy):", dna_sequence_copy)

#     dna_sequence_weighted = generate_dna_sequence_weighted(alphabet1, alphabet2, probabilities, length)
#     print("DNA Sequence (Weighted):", dna_sequence_weighted)

# if __name__ == "__main__":
#     main()

import argparse
import random

# Constants for linear congruential generator
IM = 139968
IA = 3877
IC = 29573
Seed = 42


def random_number(seed, im, ia, ic):
    local_seed = seed
    while True:
        local_seed = (local_seed * ia + ic) % im
        yield local_seed

def generate_dna_sequence_copy(source_sequence, length, seed):
    sequence = ""
    source_length = len(source_sequence)
    prng = random_number(seed, IM, IA, IC)
    for _ in range(length):
        index = next(prng) % source_length
        sequence += source_sequence[index]
    return sequence

def generate_dna_sequence_weighted(alphabet1, alphabet2, probabilities, length, seed):
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    sequence = ""
    prng = random_number(seed, IM, IA, IC)
    for _ in range(length):
        rand_num = next(prng) / IM
        for i, cum_prob in enumerate(cumulative_probabilities):
            if rand_num <= cum_prob:
                sequence += alphabet1[i] if i < len(alphabet1) else alphabet2[i - len(alphabet1)]
                break
    return sequence

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate DNA sequences")
    parser.add_argument("length", type=int, help="Length of the DNA sequence")
    args = parser.parse_args()

    source_sequence = "AGCT"
    length = args.length
    alphabet1 = "AC"
    alphabet2 = "GT"
    probabilities = [0.3, 0.2]
    seed = 42  # You can change the seed value if needed

    dna_sequence_copy = generate_dna_sequence_copy(source_sequence, length, seed)
    print("DNA Sequence (Copy):", dna_sequence_copy)

    dna_sequence_weighted = generate_dna_sequence_weighted(alphabet1, alphabet2, probabilities, length, seed)
    print("DNA Sequence (Weighted):", dna_sequence_weighted)
