#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, sid):
        self.name, self.address, self.sid = name, address, sid
        self.scores = {}

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}'

    def add_mark(self, module, mark):
        if mark >= 0:
            self.scores[module] = mark

    def get_mark(self, module):
        return self.scores[module] if module in self.scores.keys() else "Not registered for module"
