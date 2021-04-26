#!/usr/bin/env python3

x = int(input())

if x % 100 == 11 or x % 100 == 12 or x % 100 == 13:
  print("th")
else:
  if x % 10 < 4 and x % 10 > 0:
    if x % 10 == 1:
      print("st")
    if x % 10 == 2:
      print("nd")
    if x % 10 == 3:
      print("rd")
  else:
    print("th")
