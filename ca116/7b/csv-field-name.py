#!/usr/bin/env python3

import sys

x = int(sys.argv[1])

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
print(a[x])
