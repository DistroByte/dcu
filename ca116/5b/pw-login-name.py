#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) - 1:
        if s[i] == ":":
            print(s[:i])
            i = len(s)
        i += 1
    s = input()
