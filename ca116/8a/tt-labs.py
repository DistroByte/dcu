#!/usr/bin/env python3

s = input()
time = 0
arr = []

while s != "end":
    time = int(s.split(" ")[2])
    if time > 1:
        arr.append(s)
    s = input()

i = 0
while i < len(arr):
    print(arr[i])
    i += 1
