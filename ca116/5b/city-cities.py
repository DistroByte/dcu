#!/usr/bin/env python3

s = input()
s = input()

while s != "end":
    i = 0
    while i < len(s) - 5:
        if s[i:i + 4] == "City":
            print(s[:i + 4])
        i += 1
    s = input()
