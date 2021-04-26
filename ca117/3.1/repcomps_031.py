#!/usr/bin/env python3

import sys


def multiples(num):
    return ["X" if x % 3 == 0 else x for x in range(1, num)]


for x in sys.stdin:
    num = int(x) + 1
    print(f'Multiples of 3 replaced: {multiples(num)}')
