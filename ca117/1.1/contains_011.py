#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    arr = line.casefold().split(" ")
    toCheck = arr[0].rstrip()
    for s in arr[1]:
        toCheck = toCheck.replace(s, "", 1)
    if len(toCheck) > 0:
        print("False")
    else:
        print("True")
