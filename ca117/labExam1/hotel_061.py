#!/usr/bin/env python3

import sys

a = [int(i) for i in sys.stdin.read().split()]
n, r = a[0], a[1:]
rooms = [0] * (n)
for i in range(0, len(r)):
    rooms[r[i] - 1] = 1
if rooms.count(0):
    print(rooms.index(0) + 1)
else:
    print('no room')
