#!/usr/bin/env python3

a = ["a", "b", "c", "d", "e", "f", "g", "h"]

i = 0
while i < len(a) // 2:
    tmp = a[i]
    a[i] = a[len(a) - i - 1]
    a[len(a) - i - 1] = tmp
    i = i + 1
