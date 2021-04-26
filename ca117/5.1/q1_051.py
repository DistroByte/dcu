#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

for line in lines:
    if len(line) % 2 == 0 and len(line) != 0:
        sList = list(line)
        sList[::2], sList[1::2] = sList[1::2], sList[::2]
        print(''.join((sList)))
    else:
        sList = list(line[:-1])
        sList[::2], sList[1::2] = sList[1::2], sList[::2]
        sList.append(line[-1])
        print(''.join((sList)))
