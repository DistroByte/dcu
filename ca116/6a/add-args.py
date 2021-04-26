#!/usr/bin/env python3

import sys

args = sys.argv[1:]
n = len(args)
i = 0
total = 0

while i < n:
    total += int(args[i])
    i += 1
print(total)
