#!/usr/bin/env python3

import sys

lines = [line.split() for line in sys.stdin]

total = {}
disqualif = []

for score in lines:
    name = score[:-3]
    first, second, third = score[-3:]
    try:
        for hole in score[-3:]:
            if int(hole) < 0:
                disqualif.append(name)
            else:
                total[" ".join(name)] = int(first) + int(second) + int(third)
    except ValueError:
        disqualif.append(" ".join(name))

total = sorted(total.items(), key=lambda item: item[1])

for k, v in total:
    print('{}: {}'.format(k, v))
if len(disqualif) > 0:
    print(f'Disqualified: {", ".join(disqualif)}')
