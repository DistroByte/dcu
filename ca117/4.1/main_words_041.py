#!/usr/bin/env python3

import sys
import string

lines = [line.casefold() for lines in sys.stdin for line in lines.split()]

formatted = []
for line in lines:
    word = ""
    for char in line:
        if char not in string.punctuation or char == "'":
            word += char
    formatted.append(word)

freq = {word: formatted.count(word)
        for word in formatted if formatted.count(word) >= 3 and len(word) > 3}


w = 0
x = 0
for entry in freq:
    if w < len(entry):
        w = len(entry)
    if x < len(str(freq[entry])):
        x = len(str(freq[entry]))

for (k, v) in sorted(freq.items()):
    print(f'{k:>{w}} : {v:>{x}}')
