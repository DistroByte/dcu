#!/usr/bin/env python3

s = input()
arr = []

while s != "end":
    arr.append(s.split(" ")[3])
    s = input()

i = 0
while i < len(arr):
    print(arr[i])
    i += 1
