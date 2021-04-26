#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

maxLen = 0
for line in lines:
    if len(line) > maxLen:
        maxLen = len(line)

for line in lines:
    toPrint = f'{line.rstrip():^{maxLen - 1}}'
    print(toPrint)
