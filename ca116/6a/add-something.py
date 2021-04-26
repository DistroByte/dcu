#!/usr/bin/env python3

a = []
n = input()

while n != "end":
    a.append(int(n))
    n = input()

x = int(input())
i = 0

while i < len(a):
    print(a[i] + x)
    i += 1
