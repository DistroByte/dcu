#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(s)
    s = input()

i = len(a) - 1
while i != -1:
    print(a[i])
    i -= 1
