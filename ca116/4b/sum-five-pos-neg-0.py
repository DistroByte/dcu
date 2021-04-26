#!/usr/bin/env python3

n = 1
i = 0
pos = 0
neg = 0

while i < n:
    x = int(input())
    if x == 0:
        i += 1
    if x > 0:
        pos += x
    else:
        neg += x

print(neg, pos)
