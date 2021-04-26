#!/usr/bin/env python3

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x = input()

while x != "end":
    x = int(x)
    a[x] += 1
    x = input()

i = 0
while i < len(a):
    print(i, a[i] * "*")
    i += 1
