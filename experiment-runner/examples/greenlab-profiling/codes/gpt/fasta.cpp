#include <algorithm>
#include <array>
#include <vector>
#include <iostream>
#include <numeric>
#include <functional>

struct IUB
{
   float p;
   char c;
};

const std::string alu =
{
  "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGG"
   "GAGGCCGAGGCGGGCGGATCACCTGAGGTCAGGAGTTCGAGA"
   "CCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAAT"
   "ACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCA"
   "GCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGG"
   "AGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCC"
   "AGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"
};

std::array<IUB,15> iub =
{{
   { 0.27f, 'a' },
   { 0.12f, 'c' },
   { 0.12f, 'g' },
   { 0.27f, 't' },
   { 0.02f, 'B' },
   { 0.02f, 'D' },
   { 0.02f, 'H' },
   { 0.02f, 'K' },
   { 0.02f, 'M' },
   { 0.02f, 'N' },
   { 0.02f, 'R' },
   { 0.02f, 'S' },
   { 0.02f, 'V' },
   { 0.02f, 'W' },
   { 0.02f, 'Y' }
}};

std::array<IUB, 4> homosapiens =
{{
   { 0.3029549426680f, 'a' },
   { 0.1979883004921f, 'c' },
   { 0.1975473066391f, 'g' },
   { 0.3015094502008f, 't' }
}};

const int IM = 139968;
const float IM_RECIPROCAL = 1.0f / IM;

uint32_t gen_random()
{
   static const int IA = 3877, IC = 29573;
   static int last = 42;
   last = (last * IA + IC) % IM;
   return last;
}

char convert_trivial(char c)
{
   return c;
}

template<class iterator_type>
char make_repeat_generator(iterator_type& current, iterator_type first, iterator_type last)
{
   if (current == last)
      current = first;
   return *current++;
}

template<class iterator_type>
char convert_random(uint32_t random, iterator_type begin, iterator_type end)
{
   const float p = random * IM_RECIPROCAL;
   auto result = std::find_if(begin, end, [p] (IUB i) { return p <= i.p; });
   return result->c;
}

char convert_IUB(uint32_t random)
{
   return convert_random(random, iub.begin(), iub.end());
}

char convert_homosapiens(uint32_t random)
{
   return convert_random(random, homosapiens.begin(), homosapiens.end());
}

template<class iterator_type>
void make_cumulative(iterator_type first, iterator_type last)
{
   std::partial_sum(first, last, first,
                [] (IUB l, IUB r) -> IUB { r.p += l.p; return r; });
}

const size_t CHARS_PER_LINE = 60;

template <class generator_type, class converter_type >
void make(const char* desc, int n, generator_type generator, converter_type converter) {
   std::cout << '>' << desc << '\n';
   
   int col = 0;
   for(int i = 0; i < n; ++i) {
      char output = converter(generator());
      std::cout << output;
      if(++col >= CHARS_PER_LINE) {
         std::cout << '\n';
         col = 0;
      }
   }
   if(col != 0) std::cout << '\n';
}

int main(int argc, char *argv[])
{
   int n = 1000;
   if (argc < 2 || (n = std::atoi(argv[1])) <= 0) {
      std::cerr << "usage: " << argv[0] << " length\n";
      return 1;
   }
   
   make_cumulative(iub.begin(), iub.end());
   make_cumulative(homosapiens.begin(), homosapiens.end());

   auto alu_iter = alu.begin();
   make("ONE Homo sapiens alu", n * 2,
       [&]() { return make_repeat_generator(alu_iter, alu.begin(), alu.end()); },
       convert_trivial );
   
   make("TWO IUB ambiguity codes", n * 3,
       [&]() { return gen_random(); },
       convert_IUB );
   
   make("THREE Homo sapiens frequency", n * 5,
       [&]() { return gen_random(); },
       convert_homosapiens );
   
   return 0;
}
