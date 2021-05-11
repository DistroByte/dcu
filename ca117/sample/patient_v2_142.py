class Patient(object):
    def __init__(self, name, age, doctor, meds):
        self.name, self.age, self.doctor, self.meds = name, age, doctor, meds

    def __str__(self):
        prettyMeds = ", ".join(self.meds)
        toPrint = f'Name: {self.name}\nAge: {self.age}\nMedications: {prettyMeds}\nDoctor: {self.doctor}'
        return toPrint
