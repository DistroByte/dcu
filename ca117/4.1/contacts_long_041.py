#!/usr/bin/env python3

import sys

contactsEmail = {word.split()[0]: word.split()[2]
                 for word in open(sys.argv[1]).readlines()}
contacts = {word.split()[0]: word.split()[1]
            for word in open(sys.argv[1]).readlines()}

for name in sys.stdin:
    name = name.strip()
    if name in contacts:
        print(f'Name: {name}')
        print(f'Phone: {contacts[name]}')
    if name in contactsEmail:
        print(f'Email: {contactsEmail[name]}')
    else:
        print(f'Name: {name}')
        print("No such contact")
