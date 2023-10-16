#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cctype>

std::string to_upper(const std::string &s) {
    std::string result = s;
    for (char &c : result) {
        c = std::toupper(c);
    }
    return result;
}

std::string read_fasta_sequence(std::istream &in, const std::string &header) {
    std::string sequence;
    std::string line;
    bool recording = false;
    while (std::getline(in, line)) {
        if (line[0] == '>') {
            if (line.find(header) != std::string::npos) {
                recording = true;
            } else {
                recording = false;
            }
        } else if (recording) {
            sequence += to_upper(line);
        }
    }
    return sequence;
}

std::unordered_map<std::string, int> count_kmers(const std::string &sequence, int k) {
    std::unordered_map<std::string, int> kmers;
    for (int i = 0; i <= sequence.length() - k; ++i) {
        kmers[sequence.substr(i, k)]++;
    }
    return kmers;
}

void display(const std::vector<std::pair<std::string, int>> &sorted_kmers, int total, int k) {
    for (const auto &pair : sorted_kmers) {
        if (k == 1 || k == 2) {
            printf("%s %.3f\n", pair.first.c_str(), 100.0 * pair.second / total);
        } else {
            printf("%d\t%s\n", pair.second, pair.first.c_str());
        }
    }
}

int main() {
    std::string sequence = read_fasta_sequence(std::cin, ">THREE");
    
    for (int k : {1, 2}) {
        auto kmers = count_kmers(sequence, k);
        int total = sequence.length() - k + 1;
        std::vector<std::pair<std::string, int>> sorted_kmers(kmers.begin(), kmers.end());
        std::sort(sorted_kmers.begin(), sorted_kmers.end(), [](const auto &a, const auto &b) {
            return a.second == b.second ? a.first < b.first : a.second > b.second;
        });
        display(sorted_kmers, total, k);
    }

    std::vector<std::string> targets = {"GGT", "GGTA", "GGTATT", "GGTATTTTAATT", "GGTATTTTAATTTATAGT"};
    for (const auto &target : targets) {
        int count = count_kmers(sequence, target.length())[to_upper(target)];
        printf("%d\t%s\n", count, to_upper(target).c_str());
    }

    return 0;
}
