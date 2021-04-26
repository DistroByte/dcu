#!/usr/bin/env python3

import sys
words = sys.stdin.read().split()
seen = {}

i = 0
while i < len(words):
    if words[i] not in seen:
        seen[words[i]] = True
    i = i + 1
print(seen)
i = 0
while i < len(seen):
    if words[i] in seen:
        print("snap: ", words[i])
    i = i + 1
