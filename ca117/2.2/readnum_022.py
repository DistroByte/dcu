#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        num = int(line.strip())
        print(f'Thank you for {num}')
        exit()
    except ValueError:
        print(f'{line.strip()} is not a number')
