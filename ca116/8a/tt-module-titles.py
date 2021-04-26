#!/usr/bin/env python3

s = input()
arr = []

while s != "end":
    tmp = s.split(" ")[5:]
    arr.append(" ".join(tmp))
    s = input()

i = 0
while i < len(arr):
    print(arr[i])
    i += 1
