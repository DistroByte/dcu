#!/usr/bin/env python3

toSplit = int(input())

num = toSplit % 10000
num = num // 100

print((num % 10) * 10 + (num // 10))
