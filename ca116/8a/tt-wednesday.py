#!/usr/bin/env python3

s = input()
arr = []

while s != "end":
    if s[0] == "3":
        arr.append(s)
    s = input()

i = 0
while i < len(arr):
    print(arr[i])
    i += 1
