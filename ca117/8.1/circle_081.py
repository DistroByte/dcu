#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def midpoint(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)


class Circle(object):
    def __init__(self, centre=Point(0, 0), radius=0):
        self.radius = radius
        self.centre = centre

    def __str__(self):
        return 'Centre: {}\nRadius: {}'.format(self.centre, self.radius)

    def __add__(self, other):
        mid = Point.midpoint(self.centre, other.centre)
        r = self.radius + other.radius
        return Circle(Point(mid.x, mid.y), r)
