#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

allVowels = [
    word for word in lines if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word]

shortestWord = allVowels[0]
for word in allVowels:
    if len(word) < len(shortestWord):
        shortestWord = word

iaryCount = [word for word in lines if word[-4:] == "iary"]

mostEs = []
current = 0
for word in lines:
    if word.count("e") > current:
        mostEs = []
        mostEs.append(word)
        current = word.count("e")
    elif word.count("e") == current:
        mostEs.append(word)

print(f'Shortest word containing all vowels: {shortestWord}')
print(f'Words ending in iary: {len(iaryCount)}')
print(f'Words with most e\'s: {mostEs}')
