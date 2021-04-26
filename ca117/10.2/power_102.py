#!/usr/bin/env python3

def power(x, y):
    return 1 if y == 0 else x * power(x, y - 1)
