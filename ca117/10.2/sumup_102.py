#!/usr/bin/env python3

def sumup(n):
    return 0 if int(n) == 0 else int(n) + sumup(int(n) - 1)
