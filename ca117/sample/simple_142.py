#!/usr/bin/env python3

[print((len(set(line)) - 3) if (len(set(line)) > 2) else 0)
 for line in __import__("sys").stdin.readlines()]
