#!/usr/bin/env python3

x = input()
n = len(x)
i = 0
t = ""

while i < n:
    t += x[n - i - 1]
    i += 1

print(t)
