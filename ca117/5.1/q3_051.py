#!/usr/bin/env python3

import sys


def upper(char):
    if char.isupper():
        return char
    return '0'


for line in sys.stdin:
    line = line.strip()
    uppers = ''.join([upper(char) for char in line])
    splits = uppers.split('0')
    print(max(splits, key=len))
