#!/usr/bin/env python3

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    if files[i][0] != ".":
        if files[i][len(files[i]) - 3:] == ".py":
            print(files[i])
    i = i + 1
