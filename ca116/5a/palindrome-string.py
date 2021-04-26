#!/usr/bin/env python3

s = input()
n = len(s) - 1
i = 0
x = 0

while i < n // 2 + 1:
    if s[i] != s[n - i]:
        x += 1
    i += 1

if x == 0:
    print('palindrome')
