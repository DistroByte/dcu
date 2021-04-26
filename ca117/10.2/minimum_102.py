#!/usr/bin/env python3

def minimum(arr):
    if not arr[1:]:
        return arr[0]
    else:
        return arr[0] if arr[0] < minimum(arr[1:]) else minimum(arr[1:])
