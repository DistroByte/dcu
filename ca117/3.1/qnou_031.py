#!/usr/bin/env python3

import sys

a = [i for i in sys.stdin.read().splitlines()]
print(
    f'Words with q but no u: {[i for i in a if "q" in i.casefold().replace("qu", "")]}')
