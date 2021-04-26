#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = int(input())

p = i
j = i + 1
while j < len(a):
    if a[j] < a[p]:
        p = j
    j = j + 1

print(p)
