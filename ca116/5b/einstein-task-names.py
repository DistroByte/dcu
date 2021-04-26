#!/usr/bin/env python3

s = input()

while s != "end":
    i = (len(s) - 1)
    while i > 0:
        if s[len(s) - 2:len(s)] == "py":
            if s[i] == "/":
                print(s[i + 1:])
                i = 0
        i -= 1
    s = input()
