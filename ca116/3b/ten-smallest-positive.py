#!/usr/bin/env python3

i = 0
n = 10
smalpos = 0

while i < n:
  x = int(input())
  if i == 0 and x > 0:
    smalpos = x
  elif x > 0 and x < smalpos:
    smalpos = x
  i += 1

print(smalpos)
