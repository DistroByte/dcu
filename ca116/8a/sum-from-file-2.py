#!/usr/bin/env python3

import sys

args = sys.argv[1:]

with open(args[0]) as file:
    lines = file.readlines()

total = 0
i = 0
while i < len(lines):
    total += int(lines[i])
    i += 1

print(total)
