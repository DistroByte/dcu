#!/usr/bin/env python3

x = input()
i = 0
n = len(x)
total = 0

while i < n:
    total += int(x[i])
    i += 1

print(total)
