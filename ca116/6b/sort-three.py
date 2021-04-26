#!/usr/bin/env python3

a = []
i = 0

while i < 3:
    x = int(input())
    a.append(x)
    i += 1

if a[0] > a[1]:
    y = a[0]
    a[0] = a[1]
    a[1] = y
if a[0] > a[2]:
    y = a[0]
    a[0] = a[2]
    a[2] = y
if a[1] > a[2]:
    y = a[1]
    a[1] = a[2]
    a[2] = y

i = 0
while i < len(a):
    print(a[i])
    i += 1
