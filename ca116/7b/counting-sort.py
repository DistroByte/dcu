#!/usr/bin/env python3

a = []
s = input()
while s != 'end':
    a.append(int(s))
    s = input()

b = []
j = 0
p = 0
i = 0

while len(b) < len(a):
    if a[p] == i:
        b.append(i)
        print(i)
    j += 1
    p = j % len(a)
    i = j // len(a)
