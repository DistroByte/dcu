#!/usr/bin/env python3

if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

i = 0
smallest = a[0]
pos = 0
while i < len(a):
    if a[i] < smallest:
        smallest = a[i]
        pos = i
    i += 1

print(pos)
