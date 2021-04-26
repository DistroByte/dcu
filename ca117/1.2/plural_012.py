#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
es1 = ['x', 's', 'z', 'o']
es2 = ['ch', 'sh']
vowels = ['a', 'e', 'i', 'o', 'u']

for word in words:
    word = word.strip()
    if word[len(word) - 1] in es1 or word[len(word) - 2:] in es2:
        print(word + 'es')
    elif word[len(word) - 2] not in vowels and word[len(word) - 1] == 'y':
        print(word[:len(word) - 1] + 'ies')
    elif word[len(word) - 1] == 'f':
        print(word[:len(word) - 1] + 'ves')
    elif word[len(word) - 2:] == 'fe':
        print(word[:len(word) - 2] + 'ves')
    else:
        print(word + 's')
