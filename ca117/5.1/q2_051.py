#!/usr/bin/env python3

import sys


def isEvil(string):
    return [char for char in string if char in 'evil'] == list('evil')


def main():
    lines = [line.strip() for line in sys.stdin]

    evil = [print(word) for word in lines if isEvil(word.casefold())]


if __name__ == '__main__':
    main()
