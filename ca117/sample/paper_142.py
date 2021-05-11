#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
    A, B = line.casefold().split()[0][0], line.casefold().split()[1][0]

    if A == B:
        print("Draw")
    elif (A == "p" and B == "r") or (A == "r" and B == "s") or (A == "s" and B == "p"):
        print("Player 1 wins")
    elif len(line) > 3:
        print("Player 2 wins")
