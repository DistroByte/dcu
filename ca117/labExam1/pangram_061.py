#!/usr/bin/env python3

import sys

lines = [line.casefold() for line in sys.stdin]


for line in lines:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in line:
        if char in alpha:
            alpha = alpha.replace(char, "")
    if len(alpha) == 0:
        print("pangram")
    else:
        print(f'missing {alpha}')
