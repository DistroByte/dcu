#!/usr/bin/env python3

s = input()
i = 1

while i < len(s):
    if s[i] == s[i - 1]:
        print(s[i - 1: i + 1])
        i = len(s)
    i += 1
