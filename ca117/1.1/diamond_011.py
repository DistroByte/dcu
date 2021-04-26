#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for x in lines:
    x = int(x)
    i = 1
    while i < x:
        print((" " * (x - i) + ("* " * i)).rstrip())
        i += 1
    while i > 0:
        print((" " * (x - i) + ("* " * i)).rstrip())
        i -= 1
