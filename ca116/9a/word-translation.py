#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()

with open("translation.txt") as f:
    translations = f.read().split()
trans = {}

i = 0
while i < len(translations):
    trans[translations[i]] = translations[i + 1]
    i += 2

i = 0
while i < len(words):
    print(trans[words[i]])
    i += 1
