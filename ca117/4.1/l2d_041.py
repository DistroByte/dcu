#!/usr/bin/env python3

import sys


def l2d(file):
    lines = file.readlines()

    dictionary = {}
    keys = lines[0].split()
    values = lines[1].split()
    i = 0
    for each in keys:
        dictionary[each] = values[i]
        i += 1
    return dictionary
