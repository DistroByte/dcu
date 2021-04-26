#!/usr/bin/env python3

slash = 0
i = 0
while i < len(s):
    if s[i] == "/":
        slash += 1
    i += 1

print(slash)
