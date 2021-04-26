#!/usr/bin/env python3

def maximum(arr):
    if not arr[1:]:
        return arr[0]
    else:
        return arr[0] if arr[0] > maximum(arr[1:]) else maximum(arr[1:])
