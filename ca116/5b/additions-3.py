#!/usr/bin/env python3

i = 0
total = 0

while total != 1000:
    x = input()
    j = 0
    while j < len(x):
        if x[j] == "+":
            total = int(x[:j]) + int(x[j:])
            print(total)
        j += 1
