#!/usr/bin/env python3

import sys


def sorter(t):
    return t[-1]


def main():
    d = {}
    skips = []
    for line in sys.stdin:
        try:
            name, marks = line.strip().split(':')
            marksList = marks.strip().split(',')
            mark = sum([int(m) for m in marksList])
            d[name] = mark
        except ValueError:
            skips.append(name)
    for k, v in sorted(d.items(), key=sorter, reverse=True):
        print('{:s} : {:d}'.format(k, v))
    print('Skipped:')
    for name in skips:
        print(name)


if __name__ == '__main__':
    main()
