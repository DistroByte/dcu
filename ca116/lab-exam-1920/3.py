#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

n = 20

coords = []

i = 0
while i < n:
    coords.append([" "] * n)
    i += 1

i = 0
while i < len(lines):
    split = lines[i].split()
    x = int(split[0])
    y = int(split[1])
    coords[y][x] = "*"
    i += 1

print(" " + "-" * n)
i = 0
while i < n:
    print("|" + "".join(coords[n - i - 1]) + "|")
    i += 1

print(" " + "-" * n)
