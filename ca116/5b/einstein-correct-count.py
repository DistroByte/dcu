#!/usr/bin/env python3

s = input()
j = 0

while s != "end":
    if (s[len(s) - 7: len(s)] == "correct"):
        if (s[len(s) - 9:len(s)] != "incorrect"):
            j += 1
    s = input()

print(j)
