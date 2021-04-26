#!/usr/bin/env python3

import sys
from math import pi

for line in sys.stdin.readlines():
    pos = int(line)
    print(f'{pi:.{pos}f}')
