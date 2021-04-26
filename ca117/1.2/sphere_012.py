#!/usr/bin/env python3

import sys
import math


def sArea(radius):
    return 4 * math.pi * radius ** 2


def sVol(radius):
    return 4 / 3 * math.pi * radius ** 3


for line in sys.stdin.readlines():
    args = line.split()
    startR = float(args[0])
    incrementR = float(args[1])
    endR = float(args[2])
    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)
    print(f'{h1:>s} {h2:>15s} {h3:>15s}')
    print(f'{h4:>s} {h5:>15s} {h6:>15s}')
    while startR <= endR:
        print(f'{startR:10.1f} {sArea(startR):15.2f} {sVol(startR):15.2f}')
        startR += incrementR
