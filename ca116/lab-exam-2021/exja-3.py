#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

first = []
second = []

i = 0
while i < len(words):
    first.append(words[i].split(" ")[0])
    second.append(words[i].split(" ")[1].rstrip())
    i += 1

i = 0
while i < len(second):
    p = i
    j = i + 1
    while j < len(second):
        if second[j] < second[p]:
            p = j
        j = j + 1

    tmp1 = second[p]
    second[p] = second[i]
    second[i] = tmp1

    tmp2 = first[p]
    first[p] = first[i]
    first[i] = tmp2

    i = i + 1

i = 0
while i < len(first):
    if first[i] != 0:
        p = i
        j = i + 1
        while j < len(first):
            if first[j] < first[p] and second[j] == second[p]:
                p = j
            j = j + 1

    tmp1 = second[p]
    second[p] = second[i]
    second[i] = tmp1

    tmp2 = first[p]
    first[p] = first[i]
    first[i] = tmp2

    i = i + 1

i = 0
while i < len(first):
    print(first[i], second[i])
    i += 1
