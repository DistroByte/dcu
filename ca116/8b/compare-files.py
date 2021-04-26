#!/usr/bin/env python3

import sys

args = sys.argv[1:]

file1 = args[0]
file2 = args[1]

with open(file1) as f1:
    a = f1.readlines()

with open(file2) as f2:
    b = f2.readlines()

if len(a) < len(b):
    print(len(b) - len(a), 0)
elif len(b) < len(a):
    print(len(a) - len(b), 0)

i = 0
while i < len(a) and i < len(b):
    sectionA = a[i]
    sectionB = b[i]
    j = 0
    while j < len(sectionA):
        if sectionA[j] != sectionB[j]:
            print(i, j)
        j += 1
    i += 1
