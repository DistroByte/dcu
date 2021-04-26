#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    path = lines[i].rstrip().split("/")
    print(path[len(path) - 1])
    i += 1
