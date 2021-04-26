#!/usr/bin/env python3

import sys

args = sys.argv[1:]

with open(args[0]) as file:
    lines = file.readlines()

# print(len(lines[0]), lines[0], len(lines[0]), lines[0].rstrip())


total = 0
i = 0
while i < len(lines):
    lines[i] = lines[i].rstrip()
    nums = lines[i].split(" ")
    j = 0
    while j < len(nums):
        if len(nums[j]) > 0:
            total += int(nums[j])
        j += 1
    i += 1

print(total)
