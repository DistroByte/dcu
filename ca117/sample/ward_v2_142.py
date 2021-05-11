#!/usr/bin/env python3

class Patient(object):
    def __init__(self, name, age, doctor, meds):
        self.name, self.age, self.doctor, self.meds = name, age, doctor, meds

    def __str__(self):
        prettyMeds = ", ".join(self.meds)
        toPrint = f'Name: {self.name}\nAge: {self.age}\nMedications: {prettyMeds}\nDoctor: {self.doctor}'
        return toPrint


class Ward(object):
    def __init__(self):
        self.patients = {}

    def __len__(self):
        return len(self.patients.items())

    def add(self, patient=Patient):
        self.patients[patient.name] = patient

    def lookup(self, query):
        return self.patients[query] if query in self.patients else None

    def remove(self, query):
        self.patients.pop(query)

    def get_patients_by_medication(self, query):
        foundPatients = []

        for name, patient in self.patients.items():
            for med in patient.meds:
                if med == query:
                    foundPatients.append(patient)

        return foundPatients
