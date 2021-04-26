#!/usr/bin/env python3

a = []
s = input()
while s != 'end':
    a.append(int(s))
    s = input()

i = 0
x = 0
while i < len(a):
    j = 1
    while i + j < len(a) and a[i + j] - a[i] < 1001:
        j += 1
    if j > x:
        x = j
    i += 1
print(x)
