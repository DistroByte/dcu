#!/usr/bin/env python3

s = input()
x = 0
y = 0

while s != "end":
    i = 0
    while i < len(s) - 2:
        if s[i] == ":":
            x = i
            i = len(s) - 2
        i += 1
    j = len(s) - 1
    while j > 0:
        if s[j] == ":":
            y = j + 1
            j = 0
        j -= 1
    print(s[:x], s[y:])
    s = input()
