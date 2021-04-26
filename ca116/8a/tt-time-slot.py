#!/usr/bin/env python3

s = input()
arr = []

while s != "end":
    arr.append(s)
    s = input()

i = 0
while i < len(arr):
    s = arr[i]
    tmp = s.split(" ")
    tmp[1] = tmp[1] + ":00 " + str((int(tmp[1]) - 1) + int(tmp[2])) + ":50"
    if tmp[1][0] == "0":
        tmp[1] = tmp[1][1:]
    tmp.pop(2)
    arr[i] = " ".join(tmp)
    i += 1

i = 0
while i < len(arr):
    print(arr[i])
    i += 1
