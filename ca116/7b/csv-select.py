#!/usr/bin/env python3

import sys

args = sys.argv[1]

head = args.split("=")

s = input()
maxCommas = 1

i = 0
while i < len(s):
    if s[i] == ",":
        maxCommas += 1
    if s[i: i + len(head[0])] == head[0]:
        i = len(s)
    i += 1

s = input()

i = 0
while s != "end":
    i = 0
    currentCommas = 0
    while i < len(s):
        if s[i] == ",":
            currentCommas += 1
        if currentCommas >= maxCommas:
            i = len(s)
        if s[i: i + len(head[1])] == head[1]:
            print(s)
            i = len(s)
        i += 1
    s = input()
