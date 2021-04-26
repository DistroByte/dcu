#!/usr/bin/env python3

import sys


def sumFac(n):
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if n // i != i:
                total += (n // i)
        i += 1
    return total - n


def isPerfect(num):
    if sumFac(int(num)) == int(num):
        return True
    return False


def main():
    [print(isPerfect(l.strip())) for l in sys.stdin]


if __name__ == '__main__':
    main()
