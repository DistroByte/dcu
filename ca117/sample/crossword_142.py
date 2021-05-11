#!/usr/bin/env python3

import sys

a, b = sys.stdin.read().strip().split()

for letter in a:
    if letter in b:
        cross = letter
        break

horiz = int(a.find(cross))
vertic = int(b.find(cross))

i = 0
while i < len(b):
    if i != vertic:
        print(("." * horiz) + b[i] + ("." * (len(a) - horiz - 1)))
    else:
        print(a)
    i += 1
