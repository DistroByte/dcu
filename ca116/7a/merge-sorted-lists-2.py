#!/usr/bin/env python3

a = []
b = []

x = input()

while x != "end":
    a.append(int(x))
    x = input()

x = input()

while x != "end":
    b.append(int(x))
    x = input()

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print(a[i])
        i += 1
    else:
        print(b[j])
        j += 1


if i == len(a):
    while j < len(b):
        print(b[j])
        j += 1
else:
    while i < len(a):
        print(a[i])
        i += 1
