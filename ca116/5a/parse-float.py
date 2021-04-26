#!/usr/bin/env python3

x = input()
i = 0

while i < len(x):
    if x[i] == ".":
        print(x[0:i])
        print(x[i + 1: len(x)])
    i += 1
