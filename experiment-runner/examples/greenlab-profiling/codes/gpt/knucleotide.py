# #!/usr/bin/python3

# import sys
# from collections import defaultdict

# def read_fasta_file():
#     data = sys.stdin.read().split("\n")
#     sequence = []
#     for line in data:
#         if not line.startswith('>'):
#             sequence.append(line)
#     return "".join(sequence).upper()  # 转换为大写

# def count_kmers(sequence, k):
#     kmers = defaultdict(int)
#     for i in range(len(sequence) - k + 1):
#         kmer = sequence[i:i+k]
#         kmers[kmer] += 1
#     return kmers

# def main():
#     sequence = read_fasta_file()

#     # Count and print 1-nucleotide and 2-nucleotide sequences
#     for k in [1, 2]:
#         kmers = count_kmers(sequence, k)
#         total = sum(kmers.values())
#         sorted_kmers = sorted(kmers.items(), key=lambda x: (-x[1], x[0]))
        
#         for kmer, count in sorted_kmers:
#             if k == 1:
#                 print("{} {:.3f}".format(kmer, 100*count/total))
#             elif k == 2:
#                 print("{} {:.3f}".format(kmer, 100*count/total))
#         print()

#     # This part remains the same
#     targets = ["GGT", "GGTA", "GGTATT", "GGTATTTTAATT", "GGTATTTTAATTTATAGT"]
#     kmers = {}
#     for k in [3, 4, 6, 12, 18]:
#         kmers.update(count_kmers(sequence, k))
    
#     for target in targets:
#         count = kmers.get(target, 0)  # 如果目标序列不在哈希表中，则返回0
#         print("{}\t{}".format(count, target))

# if __name__ == "__main__":
#     main()

#!/usr/bin/python3

import sys
from collections import defaultdict

def read_fasta_sequence(file, header):
    sequence = []
    recording = False
    for line in file:
        if line.startswith('>'):
            if header in line:
                recording = True
            else:
                recording = False
        elif recording:
            sequence.append(line.strip().upper())
    return ''.join(sequence)

def count_kmers(sequence, k):
    kmers = defaultdict(int)
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers[kmer] += 1
    return kmers

def display(sorted_kmers, total, k):
    for kmer, count in sorted_kmers:
        if k == 1 or k == 2:
            print("{} {:.3f}".format(kmer, 100*count/total))
        else:
            print("{}\t{}".format(count, kmer))

def main():
    sequence = read_fasta_sequence(sys.stdin, '>THREE')
    
    for k in [1, 2]:
        kmers = count_kmers(sequence, k)
        total = len(sequence) - k + 1
        sorted_kmers = sorted(kmers.items(), key=lambda x: (-x[1], x[0]))
        display(sorted_kmers, total, k)

    targets = ["GGT", "GGTA", "GGTATT", "GGTATTTTAATT", "GGTATTTTAATTTATAGT"]
    for target in targets:
        count = count_kmers(sequence, len(target)).get(target, 0)
        print("{}\t{}".format(count, target))

if __name__ == "__main__":
    main()
