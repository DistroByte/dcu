#!/usr/bin/env python3

import sys

words = sys.stdin.readline().split('"')

if 2 < len(words):
    print(words[1])
