#!/usr/bin/env python3

s = input()
n = len(s)
i = 0

while i < n - 1:
    if s[i] != " ":
        print(i)
        i = n
    elif i == n - 2:
        print("-1")
    i += 1
