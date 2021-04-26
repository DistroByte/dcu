#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and (s[i] < "@" or "[" < s[i]):
    i += 1

if i < len(s):
    j = i
    while j < len(s) and ("A" <= s[j] or s[j] >= "Z"):
        j += 1
    print(s[i:j], i)
