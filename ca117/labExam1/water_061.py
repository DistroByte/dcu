#!/usr/bin/env python3

import sys

litres, capacities = [line.strip() for line in sys.stdin]
capacity = [num for num in capacities.split()]

total = int(litres)
filled = 0
for num in capacity:
    total -= int(num)
    if total < 0:
        break
    else:
        filled += 1
print(filled)
