#!/usr/bin/env python3

import sys

contacts = {word.split()[0]: word.split()[1]
            for word in open(sys.argv[1]).readlines()}

for name in sys.stdin:
    name = name.strip()
    if name in contacts:
        print(f'Name: {name}')
        print(f'Phone: {contacts[name]}')
    else:
        print(f'Name: {name}')
        print("No such contact")
