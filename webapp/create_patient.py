from faker import Faker


def Create_patient():
    patient = Faker("ru_RU")
    patient_list = patient.name().split()
    return {'first_name': patient_list[1],
            'last_name': patient_list[0],
            "age": patient.date_of_birth(minimum_age=18, maximum_age=70),
            'address': patient.street_address()
            }

