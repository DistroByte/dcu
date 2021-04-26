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

freq = {word: formatted.count(word) for word in formatted}
for (k, v) in sorted(freq.items()):
    print('{} : {}'.format(k, v))
