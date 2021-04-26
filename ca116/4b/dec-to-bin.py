#!/usr/bin/env python3

n = int(input())
b = 0
i = 0

while n != 0:
    r = n % 2
    n = n // 2
    b = (r * (10 ** i)) + b
    i += 1

print(b)
