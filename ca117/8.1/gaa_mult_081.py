#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

    def score2points(self):
        return self.goals * 3 + self.points

    def __eq__(self, other):
        return self.score2points() == other.score2points()

    def __gt__(self, other):
        return self.score2points() > other.score2points()

    def __lt__(self, other):
        return self.score2points() < other.score2points()

    def __le__(self, other):
        return self.score2points() <= other.score2points()

    def __ge__(self, other):
        return self.score2points() >= other.score2points()

    def __add__(self, other):
        tg = self.goals + other.goals
        tc = self.points + other.points
        return Score(tg, tc)

    def __sub__(self, other):
        tg = self.goals - other.goals
        tc = self.points - other.points
        return Score(tg, tc)

    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points
        return self

    def __isub__(self, other):
        self.goals -= other.goals
        self.points -= other.points
        return self

    def __mul__(self, other):
        mulg = self.goals * int(other)
        mulp = self.points * (other)
        return Score(mulg, mulp)

    def __rmul__(self, other):
        return Score(self.goals * other, self.points * other)

    def __imul__(self, other):
        self.goals *= other
        self.points *= other
        return self
