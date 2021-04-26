#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    nums = line.split()
    base = int(nums[1])
    toConvert = nums[0]
    total = 0
    i = 0
    while i < len(toConvert):
        total += int(toConvert[len(toConvert) - i - 1]) * (base ** i)
        i += 1
    print(total)
