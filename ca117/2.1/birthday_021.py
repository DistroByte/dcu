#!/usr/bin/env python3

import sys
import calendar
lines = sys.stdin.readlines()

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

poem = ["Monday's child is fair of face",
        "Tuesday's child is full of grace",
        "Wednesday's child is full of woe",
        "Thursday's child has far to go",
        "Friday's child is loving and giving",
        "Saturday's child works hard for a living",
        "Sunday's child is fair and wise and good in every way"
        ]


def getDay(date):
    day, month, year = date.split()
    return days[calendar.weekday(int(year), int(month), int(day))]


def getLine(date):
    day, month, year = date.split()
    return poem[calendar.weekday(int(year), int(month), int(day))]


for line in lines:
    print(f'You were born on a {getDay(line)} and {getLine(line)}.')
