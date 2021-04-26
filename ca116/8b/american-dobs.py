#!/usr/bin/env python3

import sys

with open("irish-dobs.txt") as f:
    lines = f.readlines()

newLines = []
i = 0
while i < len(lines):
    words = lines[i].rstrip().split(" ")
    dates = words[0].split("/")
    dateNew = dates[1] + "/" + dates[0] + "/" + dates[2]
    words[0] = dateNew
    newLines.append(" ".join(words) + "\n")
    i += 1

with open("american-dobs.txt", "w") as w:
    w.write("".join(newLines))
