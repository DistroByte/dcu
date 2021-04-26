#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    names = line.rstrip().split(".")
    lastNameNum = names[1][0: names[1].index("@")].capitalize()
    print(names[0].capitalize(), "".join(
        [i for i in lastNameNum if not i.isdigit()]))
