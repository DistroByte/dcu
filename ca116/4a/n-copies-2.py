#!/usr/bin/env python3

x = input() + "-"
l = len(x)
n = int(input())
i = 0

out = x * n
print(out[0:len(out) - 1])
