#!/usr/bin/env python3

n = int(input())
h = ""
i = 0
strings = "0123456789abcdef"

while n != 0:
    r = strings[n % 16]
    n = n // 16
    h = r + h
    i += 1

print(h)
