#!/usr/bin/env python3

s = input()
i = 0
while i < len(s):
    x = s[i]
    if x.isupper():
        print(i)
        i = len(s)
    i += 1
