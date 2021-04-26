#!/usr/bin/env python3

i = 0
n = 9
smallest = int(input())

while i < n:
  x = int(input())
  if x < smallest:
    smallest = x
  i += 1

print(smallest)
