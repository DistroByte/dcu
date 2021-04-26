#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()


def procFile(left, right):
    if len(right) != len(left):
        return False

    for char in left:
        right = right.replace(char, "", 1)
    if len(right) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    for line in lines:
        args = line.casefold().split()
        print(procFile(args[0], args[1]))
