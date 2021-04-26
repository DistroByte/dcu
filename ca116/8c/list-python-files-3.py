#!/usr/bin/env python3

import os
files = os.listdir(".")

shebang = "#!/usr/bin/env python3\n"

i = 0
while i < len(files):
    if files[i][0] != ".":
        with open(files[i]) as f:
            line = f.readline()
        if len(line) > 0:
            x = files[i][len(files[i]) - 3:]
            if x == ".py":
                print(files[i])
            elif line == shebang:
                print(files[i])
    i += 1
