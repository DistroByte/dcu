#!/usr/bin/env python3

import sys


def getMedian(arr, listLen):
    if listLen % 2 == 1:
        return nums[listLen // 2]
    else:
        return (nums[listLen // 2] + nums[listLen // 2 - 1]) / 2


nums = sorted([int(line.strip()) for line in sys.stdin])
listLen = len(nums)

print('Mean: {:.1f}'.format(sum(nums) / listLen))
print('Median: {:.1f}'.format(getMedian(nums, listLen)))
