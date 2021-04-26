#!/usr/bin/env python3

n = 5
i = 0
total = 0

while i < n:
    x = int(input())
    if x > 0:
        total += x
    else:
        total += -x
    i += 1

print(total)
