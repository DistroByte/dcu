#!/usr/bin/env python3

import sys
fileName = sys.argv[1]
n = sys.argv[1:]

with open(fileName, "w") as f:
    i = 1
    while i < len(n):
        f.write(n[i] + "\n")
        i = i + 1
