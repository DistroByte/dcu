#!/usr/bin/env python3

i = 0
n = 10
stored = 0

while i < n:
  x = int(input())
  stored = stored + (x * (10 ** i))
  i += 1

while n > i - 10:
  print((stored // (10 ** (n - 1))) % 10)
  n -= 1
