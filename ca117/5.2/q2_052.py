#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()


def makeInt(list):
    nums = []
    for x in list:
        nums.append(int(x))
    nums.sort(reverse=True)
    return nums


nums = makeInt(lines[0].split())
order = lines[1]


def printOrder(order, numbers):
    A, B, C, D = numbers
    orderDict = {}
    for char in order:
        if char == "A":
            orderDict[int(A)] = char
        if char == "B":
            orderDict[int(B)] = char
        if char == "C":
            orderDict[int(C)] = char
        if char == "D":
            orderDict[int(D)] = char
    final = ""
    for num in orderDict:
        final += " " + str(num)
    print(final.strip())


printOrder(order, nums)
