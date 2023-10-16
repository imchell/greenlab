#include <iostream>
#include <mpfr.h>

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    std::cerr << "Usage: " << argv[0] << " [number_of_digits]" << std::endl;
    return 1;
  }

  int digits = std::stoi(argv[1]);
  mpfr_t pi;
  mpfr_init2(pi, digits * 3.44); // 3.44 is a conversion factor from base-10 to base-2 digits
  mpfr_const_pi(pi, MPFR_RNDN);
  mpfr_exp_t exponent;
  char *pi_str = mpfr_get_str(NULL, &exponent, 10, 0, pi, MPFR_RNDN);
  std::cout << pi_str[0] << "." << (pi_str + 1) << std::endl;
  mpfr_free_str(pi_str);
  mpfr_clear(pi);

  return 0;
}
