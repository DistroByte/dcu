#!/usr/bin/env python3

i = 0
n = 9
largest = int(input())

while i < n:
  x = int(input())
  if x > largest:
    largest = x
  i += 1

print(largest)
