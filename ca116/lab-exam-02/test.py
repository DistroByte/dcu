#!/usr/bin/env python3

a = [16578, 12977, 25661, 16342, 42]
total = 0

i = 0
while i < len(a):
    total = total + (int(input()) - a[i])
    i = i + 1

print(total)
