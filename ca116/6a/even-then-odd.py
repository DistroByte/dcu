#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    if int(s) % 2 == 0:
        print(int(s))
    else:
        a.append(int(s))
    s = input()

i = 0
while i < len(a):
    print(a[i])
    i += 1
