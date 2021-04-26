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

    def get_avg(self):
        return sum(self.scores.values()) / len(self.scores.keys()) if len(self.scores.keys()) > 0 else 0

    def __eq__(self, other):
        return self.get_avg() == other.get_avg()

    def __gt__(self, other):
        return self.get_avg() > other.get_avg()

    def __lt__(self, other):
        return self.get_avg() < other.get_avg()


class Classlist(object):
    def __init__(self):
        self.list = {}

    def sorter(t):
        return t[1].sid

    def __str__(self):
        toPrint = []
        for (sid, obj) in sorted(self.list.items(), key=Classlist.sorter):
            toPrint.append(obj.__str__())
        return '\n'.join(toPrint)

    def add(self, student):
        self.list[student.sid] = student

    def lookup(self, sid):
        return self.list[sid] if sid in self.list.keys() else None

    def remove(self, sid):
        self.list.pop(sid) if sid in self.list.keys() else None
