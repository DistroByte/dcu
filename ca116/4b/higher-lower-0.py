#!/usr/bin/env python3

x = int(input())

while x != 0:
    y = int(input())
    if y == 0:
        x = y
    elif x > y:
        print("lower")
        x = y
    elif x < y:
        print("higher")
        x = y
    elif x == y:
        print("equal")
        x = y
