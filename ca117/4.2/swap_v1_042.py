#!/usr/bin/env python3

def swap_keys_values(dictionary):
    swapped = {v: k for (k, v) in dictionary.items()}
    return swapped
