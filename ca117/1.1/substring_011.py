#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    print(line.casefold().split(" ")[0] in line.casefold().split(" ")[1])
