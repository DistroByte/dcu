#!/usr/bin/env python3

a = int(input())
b = int(input())
x = 0

while b != 0:
    x = b
    b = a % b
    a = x

print(a)
