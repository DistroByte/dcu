#!/usr/bin/env python3

import sys


def seconds(t):
    [mins, secs] = t.split(':')
    total = int(mins) * 60 + int(secs)
    return total


def sorter(t):
    return seconds(t[-1])


def main():
    d = {}
    for line in sys.stdin:
        try:
            args = line.split()
            name, times = args[0], args[1:]
            d[name] = min(times, key=seconds)
        except ValueError:
            continue
    winner = min(d.items(), key=sorter)
    name, time = winner
    print('{} : {}'.format(name, time))


if __name__ == '__main__':
    main()
