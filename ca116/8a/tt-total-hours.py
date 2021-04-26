#!/usr/bin/env python3

s = input()
time = 0

while s != "end":
    time = time + int(s.split(" ")[2])
    s = input()

print(time)
