#!/usr/bin/env python3

import sys

content = [word.strip() for word in sys.stdin.readlines()]

censor = []
with open(sys.argv[1]) as f:
    censor = [line.strip() for line in f.readlines()]

for line in content:
    for censorWord in censor:
        if censorWord in line:
            line = line.replace(censorWord, "@" * len(censorWord))
    print(line)
