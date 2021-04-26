#!/usr/bin/env python3

import sys

args = sys.argv[1:]
n = int(args[0])

i = 1
while i < n:
    s = ((n - i) // 2)
    print((s * " ") + (i * "*"))
    i += 2

while i > 0:
    s = ((n - i) // 2)
    print((s * " ") + (i * "*"))
    i -= 2
