#!/usr/bin/env python3

import sys

first_argument = sys.argv[1]
args = sys.argv[1:]

i = 0
while i < len(args):
    if int(args[i]) > 500:
        print(args[i])
    i += 1
