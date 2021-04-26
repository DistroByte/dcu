#!/usr/bin/env python3

import sys


def sorter(t):
    return t[-1]


def makeDictionary(f):
    d = {}
    with open(f, 'r') as fin:
        for line in fin:
            food, calories = line.strip().rsplit(maxsplit=1)
            d[food] = int(calories)
    return d


def main():
    d = makeDictionary(sys.argv[1])

    p = {}
    for line in sys.stdin:
        tokens = line.strip().split(',')
        name, foods = tokens[0], tokens[1:]
        p[name] = 0
        for food in foods:
            if food in d:
                p[name] += d[food]
            else:
                p[name] += 100

    maxn = len(max(p.keys(), key=len))
    maxc = len(str(max(p.values())))

    for k, v in sorted(p.items(), key=sorter):
        print('{:>{:d}s} : {:{:d}d}'.format(k, maxn, v, maxc))


if __name__ == '__main__':
    main()
