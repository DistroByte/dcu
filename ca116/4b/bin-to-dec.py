#!/usr/bin/env python3

s = input()
n = len(s) - 1
total = 0
i = 0

while i < len(s):
    x = int(s[n]) * (2 ** i)
    total += x
    n -= 1
    i += 1

print(total)
