#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

totals = [0] * 11
words = ["nothing", "one pair", "two pairs",
         "three of a kind", "a straight", "a flush",
         "a full house", "four of a kind", "a straight flush", "a royal flush"
         ]


def addScore(hand):
    scores = hand.split(",")
    rank = int(scores[-1])
    totals[rank] += 1
    totals[10] += 1


for line in lines:
    addScore(line)

i = 0
for word in words:
    print(
        f'The probability of {word} is {(totals[i] / totals[10]) * 100:.4f}%')
    i += 1
