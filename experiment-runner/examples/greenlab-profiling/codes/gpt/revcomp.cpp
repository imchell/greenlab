#include <iostream>
#include <string>
#include <map>
#include <vector>

std::string reverse_complement(const std::string& sequence) {
    static std::map<char, char> complement = {
        {'A', 'T'}, {'C', 'G'}, {'G', 'C'}, {'T', 'A'},
        {'M', 'K'}, {'R', 'Y'}, {'W', 'W'}, {'S', 'S'},
        {'Y', 'R'}, {'K', 'M'}, {'V', 'B'}, {'H', 'D'},
        {'D', 'H'}, {'B', 'V'}, {'N', 'N'},
        {'a', 'T'}, {'c', 'G'}, {'g', 'C'}, {'t', 'A'},
        {'m', 'K'}, {'r', 'Y'}, {'w', 'W'}, {'s', 'S'},
        {'y', 'R'}, {'k', 'M'}, {'v', 'B'}, {'h', 'D'},
        {'d', 'H'}, {'b', 'V'}, {'n', 'N'}
    };

    std::string result;
    for (auto it = sequence.rbegin(); it != sequence.rend(); ++it) {
        result.push_back(complement[*it]);
    }

    return result;
}

int main() {
    std::string line;
    std::vector<std::string> sequences;

    while (std::getline(std::cin, line)) {
        if (line[0] == '>') {
            if (!sequences.empty()) {
                std::cout << line << std::endl;
                sequences.clear();
            } else {
                std::cout << line << std::endl;
            }
        } else {
            sequences.push_back(line);
        }
    }

    for (const auto& seq : sequences) {
        std::cout << reverse_complement(seq) << std::endl;
    }

    return 0;
}
