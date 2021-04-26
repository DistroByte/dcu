#!/usr/bin/env python3

from math import sqrt


def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    if distance - r1 - r2 < 0:
        return True
    return False
