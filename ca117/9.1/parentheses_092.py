#!/usr/bin/env python3

def matcher(line):
    s = Stack()

    for char in line:
        if char in "({[":
            s.push(char)
        else:
            if not s:
                return False
            cur = s.pop()
            if cur == '(' and char != ")" or cur == '{' and char != "}" or cur == '[' and char != "]":
                return False
    return False if s else True


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
