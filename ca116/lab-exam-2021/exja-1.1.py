#!/usr/bin/env python3

x = 1
i = 0
while i < len(a):
    if a[i] < 0:
        digit = 3
        a[i] = -a[i]
        x = -1
    else:
        digit = 3
    if a[i] % 10 == digit:
        print(a[i] * x)
    i = i + 1
