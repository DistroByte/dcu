#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line[0].capitalize() + line[1:].rstrip()
    if len(line) > 1:
        print(line[:len(line) - 1] + line[-1].capitalize())
