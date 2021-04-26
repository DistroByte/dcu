#!/usr/bin/env python3

import sys

final = []
lines = []

for line in sys.stdin:
    lines.append(line.strip())


def checkA(word):
    return len([char for char in word if "a" in char.lower()])


def checkQ(word):
    return len([char for char in word if "q" in char.lower()])


def anagram(word):
    if word == "angle":
        return
    toCheck = word.casefold()
    for s in "angle":
        toCheck = toCheck.replace(s, "", 1)
    if len(toCheck) > 0:
        return False
    else:
        return True


print(
    f'Words containing 17 letters: {[word for word in lines if len(word) == 17]}')
print(
    f'Words containing 18+ letters: {[word for word in lines if len(word) >= 18]}')
print(
    f'Words with 4 a\'s: {[word for word in lines if checkA(word) == 4]}')
print(f'Words with 2+ q\'s: {[word for word in lines if checkQ(word) >= 2]}')
print(
    f'Words containing cie: {[word for word in lines if "cie" in word]}')
print(
    f'Anagrams of angle: {[word for word in lines if len(word) == len("angle") and anagram(word)]}')
