#!/usr/bin/env python3

s = input()
n = len(s)
i = 0

while i < n - 1:
    if "A" <= s[i] and s[i] <= "Z":
        print(s[i], i)
        i = n
    i += 1
