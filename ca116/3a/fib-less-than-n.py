#!/usr/bin/env python3

x = int(input())
n1 = 0
n2 = 1

while n1 < x:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
