#!/usr/bin/env python3

with open("numbers.txt") as file:
    lines = file.readlines()

total = 0
i = 0
while i < len(lines):
    total += int(lines[i])
    i += 1

print(total)
