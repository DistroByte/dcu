#!/usr/bin/env python3

import sys

fileName = sys.argv[1]

with open(fileName) as f:
    sys.stdout.write(f.read())
