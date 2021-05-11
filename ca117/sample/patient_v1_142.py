class Patient(object):

    def __init__(self, name, age, doctor):
        self.name, self.age, self.doctor = name, age, doctor

    def __str__(self):
        toPrint = f'Name: {self.name}\nAge: {self.age}\nDoctor: {self.doctor}'
        return toPrint
