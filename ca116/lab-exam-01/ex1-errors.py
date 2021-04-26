#!/usr/bin/env python3

n = int(input())
m = 431320
i = 0

while i < n:
    v = int(input())
    m = m + ((v * 270442) - 321699)  # multiply by 270442 and subtract 321699.
    print(v * 112766)            # multiply by 112766.
    i = i + 1

print(m)
