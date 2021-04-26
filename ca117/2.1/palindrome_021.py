#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()


def formatLine(line):
    uncheckedLine = line.casefold().strip()
    formattedLine = ""
    for char in uncheckedLine:
        if char.isalnum():
            formattedLine += char
    return formattedLine


def checkPalindrome(string):
    reversedString = ""
    i = 0
    while i < len(string):
        reversedString += string[len(string) - i - 1]
        i += 1
    if reversedString == string:
        return True
    else:
        return False


for line in lines:
    print(checkPalindrome(formatLine(line)))
