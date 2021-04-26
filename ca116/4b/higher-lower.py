#!/usr/bin/env python3

x = int(input())
n = 5
i = 0

while i < n:
    y = int(input())
    if y > x:
        print("higher")
    elif y < x:
        print("lower")
    else:
        print("equal")
    x = y
    i += 1
