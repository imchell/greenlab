#include <iostream>
#include <string>
#include <vector>
#include <regex>

int main() {
    // Read the entire input
    std::string data(std::istreambuf_iterator<char>(std::cin), {});

    // Record the initial sequence length
    size_t initial_length = data.size();

    // Remove FASTA sequence descriptions and linefeed characters
    std::regex fasta_remove(">.*\n|\n");
    data = std::regex_replace(data, fasta_remove, "");
    size_t processed_length = data.size();

    // Patterns representing DNA 8-mers
    std::vector<std::string> dna_patterns = {
        "agggtaaa|tttaccct",
        "[cgt]gggtaaa|tttaccc[acg]",
        "a[act]ggtaaa|tttacc[agt]t",
        "ag[act]gtaaa|tttac[agt]ct",
        "agg[act]taaa|ttta[agt]cct",
        "aggg[acg]aaa|ttt[cgt]ccct",
        "agggt[cgt]aa|tt[acg]accct",
        "agggta[cgt]a|t[acg]taccct",
        "agggtaa[cgt]|[acg]ttaccct"
    };

    // Count matches for each pattern
    for (const auto& pattern : dna_patterns) {
        std::regex rgx(pattern);
        auto words_begin = std::sregex_iterator(data.begin(), data.end(), rgx);
        auto words_end = std::sregex_iterator();
        size_t count = std::distance(words_begin, words_end);
        std::cout << pattern << " " << count << std::endl;
    }

    // Magic patterns and their replacements
    std::vector<std::pair<std::string, std::string>> magic_patterns = {
        {"tHa[Nt]", "<4>"},
        {"aND|caN|Ha[DS]|WaS", "<3>"},
        {"a[NSt]|BY", "<2>"},
        {"<[^>]*>", "|"},
        {"\\|[^|][^|]*\\|", "-"}
    };

    // Match and replace for each magic pattern
    for (const auto& p : magic_patterns) {
        std::regex rgx(p.first);
        data = std::regex_replace(data, rgx, p.second);
    }

    size_t magic_processed_length = data.size();

    // Print the 3 recorded sequence lengths
    std::cout << std::endl;
    std::cout << initial_length << std::endl;
    std::cout << processed_length << std::endl;
    std::cout << magic_processed_length << std::endl;

    return 0;
}
