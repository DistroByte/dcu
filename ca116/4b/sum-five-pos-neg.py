#!/usr/bin/env python3

n = 5
i = 0
pos = 0
neg = 0

while i < n:
    x = int(input())
    if x > 0:
        pos += x
    else:
        neg += x
    i += 1

print(neg, pos)
