#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(s)
    s = input()

n = int(input())
p = 0
while p < len(a):
    x = 0
    i = 0
    j = 0
    while i < len(a[p]):
        while i < len(a[p]) and a[p][i] != ',':
            i += 1
        if x == n:
            print(a[p][j:i])
            i = len(a[p])
        x += 1
        i += 1
        j = i
    p += 1
