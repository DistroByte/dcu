#!/usr/bin/env python3

import sys

line = sys.stdin.read()

total = 0
i = 0
while i < len(line):
    if "A" <= line[i] and line[i] <= "Z":
        total += 1
    i += 1

print(total)
