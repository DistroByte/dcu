#!/usr/bin/env python3

import sys

nums = sys.stdin.read().rstrip().split()

i = 0
n = len(nums)

while i < n:
    if int(nums[i]) >= 100:
        print(nums[i])
        i = n
    if i == n - 1:
        print("none")
    i += 1
