#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    i = 0
    while i < len(a):
        if s == a[i]:
            i = len(a) + 1
        else:
            i += 1
    if i == len(a):
        a.append(s)
    s = input()

i = 0
while i < len(a):
    print(a[i])
    i += 1
