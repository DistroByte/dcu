#!/usr/bin/env python3

if __name__ == "__main__":
    a = [8, 9, 4, 7, 2, 11]

first = a[0]
last = a[len(a) - 1]

a[0] = last
a[len(a) - 1] = first
