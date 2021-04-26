#!/usr/bin/env python3

toSplit = int(input())

num1 = (toSplit // 100 % 10)
num2 = (toSplit // 10 % 10)
num3 = (toSplit // 1 % 10)

print(num1)
print(num2)
print(num3)
