#!/usr/bin/env python3

import sys
import string
lines = sys.stdin.read()


def removePunctuation(word):
    cleanString = ""
    for char in word:
        if char not in string.punctuation and char.isalnum():
            cleanString += char
    return cleanString


def splitString(word):
    args = word.casefold().split()
    return args


tokens = []
for word in splitString(lines):
    cleanWord = removePunctuation(word)
    if cleanWord not in tokens and len(cleanWord) > 0:
        tokens.append(cleanWord)

print(len(tokens))
