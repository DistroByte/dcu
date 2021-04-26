#!/usr/bin/env python3

def fibonacci(n):
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
