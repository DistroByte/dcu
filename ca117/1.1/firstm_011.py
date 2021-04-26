#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    words = line.split()
    final = []
    i = 0
    for word in words:
        if word[0] == "m" and i == 0:
            final.append(word.capitalize())
            i += 1
        else:
            final.append(word)
    print(" ".join(final))
