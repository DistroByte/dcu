#!/usr/bin/env python3

import sys
from math import sqrt


def main():
    lines = [l.split() for l in sys.stdin]

    for l in lines:
        a, b, c = int(l[0]), int(l[1]), int(l[2])
        if b * b < 4 * a * c:
            print('None')
        else:
            r1 = (- b + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
            r2 = (- b - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
            print(f'r1 = {r1}, r2 = {r2}')


if __name__ == '__main__':
    main()
