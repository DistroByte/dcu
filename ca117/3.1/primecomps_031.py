#!/usr/bin/env python3

import sys


for x in sys.stdin:
    num = int(x) + 1
    print(
        f'Primes: {[x for x in range(2, num) if all(x % y != 0 for y in range(2, x))]}')
