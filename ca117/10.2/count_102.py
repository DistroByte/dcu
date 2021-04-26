#!/usr/bin/env python3

def count_letters(s):
    return 0 if s == '' else 1 + count_letters(s[1:])
