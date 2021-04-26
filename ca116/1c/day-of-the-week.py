#!/usr/bin/env python3

month = int(input())
day = int(input())

yearDay = ((month - 1) * 30) + day

dayOfWeek = yearDay % 7

if dayOfWeek == 0:
  dayOfWeek = 7

print(dayOfWeek)
