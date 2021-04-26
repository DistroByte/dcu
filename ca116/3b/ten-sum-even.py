#!/usr/bin/env python3

i = 0
n = 10
total = 0

while i < n:
  x = int(input())
  total = total + ((x + 1) % 2 * x)
  i += 1

print(total)
