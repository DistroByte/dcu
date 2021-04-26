#!/usr/bin/env python3

toSplit = int(input())

date = toSplit % 10000
date = date // 100

month = toSplit % 1000000
month = month // 10000

year = toSplit % 100
year = year // 1

print((date * 10000) + (month * 100) + (year * 1))
