#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    words = line.split()
    final = []
    for word in words:
        final.append(word[:1] + word[-1].capitalize())
    print(" ".join(final))
