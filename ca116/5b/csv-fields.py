#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
    if s[i] == ",":
        print(s[:i])
        s = s[i + 1:]
        i = 0
    i += 1

j = 0
while j != 1:
    print(s)
    j = 1
