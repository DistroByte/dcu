#!/usr/bin/env python3

import sys

first_argument = sys.argv[1]
args = sys.argv[1:]

i = 0
while i < int(args[0]):
    print(i * " " + ".")
    i += 1
