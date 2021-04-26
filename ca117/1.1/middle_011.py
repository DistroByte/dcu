#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.rstrip()
    if len(line) % 2 == 0:
        print("No middle character!")
    else:
        print(line[len(line) // 2])
