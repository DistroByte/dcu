#!/usr/bin/env python3

class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'


class ContactList(object):
    def __init__(self, d={}):
        self.d = d

    def add_contact(self, contact):
        self.d[contact.name] = contact

    def del_contact(self, name):
        self.d.pop(name) if name in self.d else None

    def get_contact(self, name):
        return self.d[name] if name in self.d else None

    def __str__(self):
        toPrint = ['Contact list', '------------']
        {toPrint.append(f'{v}') for k, v in sorted(self.d.items())}
        return '\n'.join(toPrint)
