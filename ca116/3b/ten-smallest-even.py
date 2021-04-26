#!/usr/bin/env python3

i = 0
n = 10
smallPosEven = 0

while i < n:
  x = int(input())
  if i == 0 and x > 0 and x % 2 == 0:
    smallPosEven = x
  elif x < smallPosEven and x % 2 == 0:
    smallPosEven = x
  i += 1

print(smallPosEven)
