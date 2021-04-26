#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {"cycle": 0, "swim": 0, "run": 0}
        self.total = 0

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}'

    def add_time(self, activity, time):
        self.times[activity] = time
        self.total += time

    def get_time(self, activity):
        return self.times[activity]

    def __eq__(self, other):
        return self.total == other.total

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total


class Triathlon(object):
    def __init__(self, d={}):
        self.athletes = d

    def sorter(t):
        return t[1].name

    def __str__(self):
        toPrint = []
        for (tid, obj) in sorted(self.athletes.items(), key=Triathlon.sorter):
            toPrint.append(obj.__str__())
        return '\n'.join(toPrint)

    def add(self, athlete):
        self.athletes[athlete.tid] = athlete

    def remove(self, tid):
        self.athletes.pop(tid)

    def lookup(self, tid):
        return self.athletes[tid] if tid in self.athletes else None
