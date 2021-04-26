#!/usr/bin/env python3

import sys
lines = sys.stdin.read()


def splitSting(string):
    args = string.split()
    return len(args)


print(splitSting(lines))
