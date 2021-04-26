#!/usr/bin/env python3

x = input()
l = len(x)

print(x[l - 1] + x[1:l - 1] + x[0])
