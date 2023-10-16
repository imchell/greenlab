#include <iostream>

class PiDigits
{
public:
  PiDigits() : q(1), r(0), t(1), k(1), n(3), l(3) {}

  int next_digit()
  {
    while (true)
    {
      if (4 * q + r - t < n * t)
      {
        int val = n;
        int temp_q = q;
        int temp_r = r;
        int temp_t = t;
        int temp_n = n;
        q = 10 * temp_q;
        r = 10 * (temp_r - temp_n * temp_t);
        t = temp_t;
        n = (10 * (3 * q + r)) / t - 10 * temp_n;
        return val;
      }
      else
      {
        int temp_q = q;
        int temp_r = r;
        int temp_t = t;
        q = k * temp_q;
        r = (2 * temp_q + temp_r) * l;
        t = temp_t * l;
        k++;
        n = (q * (7 * k + 2) + r * l) / (t * l);
        l += 2;
      }
    }
  }

private:
  long q, r, t, k, n, l;
};

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    std::cerr << "Usage: " << argv[0] << " [number_of_digits]" << std::endl;
    return 1;
  }

  int digits = std::stoi(argv[1]);
  int count = 0;
  PiDigits pi_gen;

  for (int i = 0; i < digits; ++i)
  {
    std::cout << pi_gen.next_digit();
    count++;
    if (count % 10 == 0)
    {
      std::cout << "\t:" << count << std::endl;
    }
  }

  if (count % 10 != 0)
  {
    std::cout << "\t:" << count << std::endl;
  }

  return 0;
}
