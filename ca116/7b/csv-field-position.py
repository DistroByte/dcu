#!/usr/bin/env python3

import sys

x = sys.argv[1]

s = input()
a = []

i = 0
n = len(s)

while i < n:
    if s[i] == ",":
        a.append(s[:i])
        s = s[i + 1:]
        i = 0
        n = len(s)
    i += 1

a.append(s)

i = 0
while i < len(a):
    if a[i] == x:
        print(i)
        i = len(a)
    i += 1
