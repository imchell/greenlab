
import sys
from fractions import Fraction

def pi_digits():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t - 10*n, l)
        else:
            q, r, t, k, n, l = (q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2)

def main():
    digits = int(sys.argv[1])
    count = 0
    for d in pi_digits():
        print(d, end='')
        count += 1
        if count % 10 == 0:
            print("\t:%d" % count)
        if count == digits:
            break
    if count % 10 != 0:
        print("\t:%d" % count)

if __name__ == "__main__":
    main()
