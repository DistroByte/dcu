#!/usr/bin/env python3

i = 0
n = 1
total = 0

while i < n:
    x = int(input())
    if x == 0:
        i += 1
    elif x > 0:
        total += x
    else:
        total += -x

print(total)
