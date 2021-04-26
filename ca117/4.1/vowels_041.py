#!/usr/bin/env python3

import sys

read = sys.stdin.read().casefold()

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for vowel in vowels:
    vowels[vowel] = read.count(str(vowel))

vowels = sorted(vowels.items(), key=lambda x: x[1], reverse=True)

w = 0
for x in vowels:
    if len(str(x[1])) > w:
        w = len(str(x[1]))

for x in vowels:
    print(f'{x[0]} : {x[1]:>{w}}')
