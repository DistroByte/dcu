#!/usr/bin/env python3

import sys


def multiples(num):
    return [x for x in range(1, num) if not x % 3]


def squared(list):
    return [x ** 2 for x in list]


def doubled(num):
    return [x * 2 for x in range(1, num) if not x % 4]


def threeOrFour(num):
    return [x for x in range(1, num) if not x % 3 or not x % 4]


def threeAndFour(num):
    return [x for x in range(1, num) if not x % 3 and not x % 4]


for x in sys.stdin:
    num = int(x) + 1
    print(f'Multiples of 3: {multiples(num)}')
    print(f'Multiples of 3 squared: {squared(multiples(num))}')
    print(f'Multiples of 4 doubled: {doubled(num)}')
    print(f'Multiples of 3 or 4: {threeOrFour(num)}')
    print(f'Multiples of 3 and 4: {threeAndFour(num)}')
