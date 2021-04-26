#!/usr/bin/env python3

x = input()
t = " "
final = ""
i = 0
n = len(x)

while i < n:
    if x[i] != t:
        final += x[i]
    i += 1

print(final)
