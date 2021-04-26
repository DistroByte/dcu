#!/usr/bin/env python3

import sys

args = sys.argv[1:]

lines = []

i = 0
while i < len(args):
    with open(args[i]) as f:
        lines += f.readlines()
    i += 1

nums = []
i = 0
while i < len(lines):
    nums += lines[i].rstrip().split(" ")
    i += 1

total = 0
i = 0
while i < len(nums):
    total += int(nums[i])
    i += 1

print(total)
