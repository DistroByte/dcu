#!/usr/bin/env python3

import sys


def procfile(filename):
    try:
        with open(filename, 'r') as f:
            bestMark = -1
            for line in f:
                try:
                    mark, name = line.strip().split(maxsplit=1)
                    mark = int(mark)

                    if mark > bestMark:
                        bestMark, bestStudent = mark, name
                except ValueError:
                    print(f'Invalid mark {mark} encountered. Skipping.')
            print(f'Best student: {bestStudent}')
            print(f'Best mark: {bestMark}')
    except FileNotFoundError:
        print(f'The file{filename} cannot be opened')


procfile(sys.argv[1])
