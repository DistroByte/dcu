#!/usr/bin/env python3

x = input()
i = 0
last = 0
total = 0
j = 0

while i < len(x):
    if x[i] == "+":
        total += int(x[last:i])
        last = i
    i += 1

while j == 0:
    print(total + int(x[last:]))
    j += 1
