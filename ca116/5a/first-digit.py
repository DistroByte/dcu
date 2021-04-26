#!/usr/bin/env python3

s = input()
n = len(s)
i = 0

while i < n - 1:
    if "0" <= s[i] and s[i] <= "9":
        print(s[i], i)
        i = n
    i += 1
