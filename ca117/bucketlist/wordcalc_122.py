#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

storedVars = {}


def calculate(args):
    output = ""
    i = 0
    for arg in args:
        try:
            if i % 2 == 0:
                output = output + storedVars[arg]
            else:
                output += arg
            i += 1
        except KeyError:
            return "unknown"
    output = str(eval(output))
    for key, value in storedVars.items():
        if value == output:
            return key
    return "unknown"


for line in lines:
    args = line.split()
    if args[0] == "def":
        storedVars[args[1]] = args[2]
    if args[0] == "clear":
        storedVars.clear()
    if args[0] == "calc":
        print(" ".join(args[1:]), calculate(args[1:-1]))
