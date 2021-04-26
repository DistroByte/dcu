#!/usr/bin/env python3

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
