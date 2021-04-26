#!/usr/bin/env python3

s = input()
arr = []

while s != "end":
    arr.append(s)
    s = input()

x = input()

i = 0
while i < len(arr):
    if arr[i][0] == x:
        print(arr[i])
    i += 1
