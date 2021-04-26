#!/usr/bin/env python3

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    with open(files[i]) as f:
        contents = f.read()
    if files[i][0] != ".":
        if files[i][len(files[i]) - 4:] != ".bak":
            with open(files[i] + ".bak", "w") as f:
                f.write(contents)
    i += 1
