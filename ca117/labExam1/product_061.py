#!/usr/bin/env python3

import sys

line = sys.stdin.read().strip()


def clean(number):
    numStr = str(number)
    cleaned = ""
    for num in numStr:
        if num != "0":
            cleaned += num
    return int(cleaned)


def multiply(number):
    numStr = str(number)
    toEval = []
    for num in numStr:
        toEval.append(num)
    return eval("*".join(toEval))


while int(line) > 9:
    if "0" in str(line):
        line = clean(line)
    else:
        line = multiply(line)
print(line)
