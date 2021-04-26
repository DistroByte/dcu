#!/usr/bin/env python3

s = input()
n = len(s)
i = 0

while i < n:
    if "A" <= s[i] and s[i] <= "Z":
        print(s[i])
        i = n
    i += 1
