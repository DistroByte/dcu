#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, sid):
        self.name, self.address, self.sid = name, address, sid

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}'
