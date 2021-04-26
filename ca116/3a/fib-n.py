#!/usr/bin/env python3

pos = int(input())

n1 = 0
n2 = 1
i = 0

while i < pos:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
  i += 1
