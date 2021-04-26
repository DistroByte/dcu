#!/usr/bin/env python3

import operator
from math import sqrt


class Stack(object):
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def negate(x):
    return -x


binops = {'+': add, '-': subtract, '*': multiply, '/': divide}
uniops = {'n': negate, 'r': sqrt}


def calculator(line):
    stack = Stack()
    for e in line.split():
        if e in binops.keys():
            y = stack.pop()
            x = stack.pop()
            stack.push(binops[e](x, y))
        elif e in uniops.keys():
            stack.push(uniops[e](stack.pop()))
        else:
            stack.push(float(e))
    return stack.top()
