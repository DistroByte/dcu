#!/usr/bin/env python3

import sys

args = sys.stdin.readlines()

total = 0

i = 0
while i < len(args):
    total += int(args[i])
    i += 1

print(total)
