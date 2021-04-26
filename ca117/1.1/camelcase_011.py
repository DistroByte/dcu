#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    arr = line.rstrip().split()
    camel = []
    for i in arr:
        camel.append(i.capitalize())
    print(" ".join(camel))
