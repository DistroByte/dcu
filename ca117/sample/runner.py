from ward_v2_142 import Patient, Ward


def main():
    p1 = Patient('Mary', 34, 'James Kildare', ['aspirin'])
    p2 = Patient('Wendy', 40, 'Gregory House', ['penicillin', 'nexium'])
    p3 = Patient('Sam', 42, 'Gregory House', ['nexium'])

    w = Ward()
    w.add(p1)
    w.add(p2)
    w.add(p3)

    # Retrieve all patients on nexium
    patient_list = w.get_patients_by_medication('nexium')
    assert(len(patient_list) == 2)
    assert(p1 not in patient_list)
    assert(p2 in patient_list)
    assert(p3 in patient_list)


if __name__ == '__main__':
    main()
