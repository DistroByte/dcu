#!/usr/bin/env python3

n = 10
i = 0

while i < n:
    x = input()
    j = 0
    while j < len(x):
        if x[j] == "+":
            print(int(x[:j]) + int(x[j:]))
        j += 1
    i += 1
