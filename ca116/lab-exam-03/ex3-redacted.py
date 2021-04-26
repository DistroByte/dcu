#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
redacted = {}

with open("banned.txt") as f:
    read = f.read().rstrip().split()

i = 0
while i < len(read):
    redacted[read[i]] = len(read[i]) * "*"
    i += 1

i = 0
while i < len(words):
    tmp = words[i].rstrip()
    lineSplit = tmp.split()
    j = 0
    while j < len(lineSplit):
        if lineSplit[j] in redacted:
            lineSplit[j] = redacted[lineSplit[j]]
        j += 1
    print(" ".join(lineSplit))
    i += 1
