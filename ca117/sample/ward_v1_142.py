#!/usr/bin/env python3

class Patient(object):
    def __init__(self, name, age, doctor):
        self.name, self.age, self.doctor = name, age, doctor

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nDoctor: {self.doctor}'


class Ward(object):
    def __init__(self):
        self.patients = {}

    def __len__(self):
        return len(self.patients)

    def add(self, patient=Patient):
        self.patients[patient.name] = patient

    def lookup(self, query):
        return self.patients[query] if query in self.patients else None

    def remove(self, query):
        self.patients.pop(query)
