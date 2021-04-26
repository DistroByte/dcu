#!/usr/bin/env python3

import sys


def swap_unique_keys_values(d):
    val = list(d.values())
    seen = {v: 1 for v in val if val.count(v) == 1}
    swapped = {v: k for (k, v) in d.items() if v in seen}
    return swapped

# my_dict = {'a': 4, 'b': 7, 'c': 10, 'd': 7}
# new_dict = swap_unique_keys_values(my_dict)
# print(sorted(new_dict.items()))
