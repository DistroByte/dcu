#!/usr/bin/env python3

import sys

integer = sys.argv[1]

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    number = lines[i].rstrip()
    if (number[len(number) - len(integer):]) != integer:
        print(number)
    i += 1
