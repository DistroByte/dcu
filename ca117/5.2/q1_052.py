#!/usr/bin/env python3

import sys
lines = [line.strip() for line in sys.stdin]

for line in lines:
    string, num = line.split()
    num = int(num) % len(string)
    print(string[-num:] + string[:-num])
