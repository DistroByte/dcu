#!/usr/bin/env python3

class Student(object):

    def __init__(self, surname, forename, sid, modlist=None):
        self.surname = surname
        self.forename = forename
        self.sid = sid
        if modlist is None:
            self.modlist = []
        else:
            self.modlist = modlist

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def print_details(self):
        print('ID: {}'.format(self.sid))
        print('Surname: {}'.format(self.surname))
        print('Forename: {}'.format(self.forename))
        print('Modules: {}'.format(' '.join(self.modlist)))
