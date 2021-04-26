#!/usr/bin/env python3

import sys


def procfile(filename):
    try:
        with open(filename, 'r') as f:
            try:
                bestMark = -1
                for line in f:
                    mark, name = line.strip().split(maxsplit=1)
                    mark = int(mark)

                    if mark > bestMark:
                        bestMark, bestStudent = mark, name
                print(f'Best student: {bestStudent}')
                print(f'Best mark: {bestMark}')
            except ValueError:
                print(f'Invalid mark {mark} encountered. Exiting.')

    except FileNotFoundError:
        print(f'The file{filename} cannot be opened')


procfile(sys.argv[1])
