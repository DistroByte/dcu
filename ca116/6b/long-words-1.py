#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
while i < len(a):
    if len(a[i]) >= 6:
        print(a[i])
    i += 1
