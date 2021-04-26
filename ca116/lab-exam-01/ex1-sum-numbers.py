#!/usr/bin/env python3

n = int(input())
i = 0
total = 0

while i < n:
    x = input()
    if x == "one":
        total += 1
    elif x == "two":
        total += 2
    elif x == "three":
        total += 3
    elif x == "four":
        total += 4
    else:
        total += 5
    i += 1

print(total)
