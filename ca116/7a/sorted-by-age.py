#!/usr/bin/env python3

s = input()

name = []
val = []

while s != 'end':
    name.append(s[9:])
    val.append(int(s[6:8]) * 10000 + int(s[3:5]) * 100 + int(s[:2]))
    s = input()

i = 0
while i < len(name):
    p = i
    j = i + 1
    while j < len(name):
        if val[j] < val[p]:
            p = j
        j += 1
    tmp = val[i]
    val[i] = val[p]
    val[p] = tmp
    tmp = name[i]
    name[i] = name[p]
    name[p] = tmp
    print(name[i])
    i += 1
