#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line.rstrip()
    if len(line[1:len(line) - 2]) > 0:
        print(line[1:len(line) - 2])
