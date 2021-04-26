#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.rstrip()
    strength = [False] * 4
    total = 0
    for char in line:
        if char.isdigit():
            strength[0] = True
        elif char.isupper():
            strength[1] = True
        elif char.islower():
            strength[2] = True
        else:
            strength[3] = True
    for val in strength:
        if val:
            total += 1

    print(total)
