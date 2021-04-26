#!/usr/bin/env python3

import sys

lines = [line.split() for line in sys.stdin]

numSet = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
          5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

for line in lines:
    toPrint = []
    for num in line:
        try:
            num = int(num)
            if num <= 10 and num >= 0:
                toPrint.append(numSet[num])
            else:
                toPrint.append("unknown")
        except ValueError:
            toPrint.append("unknown")

    print(" ".join(toPrint))
