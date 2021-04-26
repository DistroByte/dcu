#!/usr/bin/env python3

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    if files[i][0] != ".":
        if files[i][len(files[i]) - 3:] == ".py":
            with open(files[i]) as f:
                lines = f.read(1)
            if len(lines) > 0:
                print(files[i])
    i += 1
