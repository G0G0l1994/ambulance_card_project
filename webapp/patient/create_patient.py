from faker import Faker


def create_patient():
    patient = Faker("ru_RU")
    patient_data = patient.name().split()
    return {'first_name': patient_data[1],
            'surname': patient_data[2],
            'last_name': patient_data[0],
            'age': patient.date_of_birth(minimum_age=18, maximum_age=70),
            'address': patient.street_address()
            }
# def save_patient():
#     patient_data = Create_patient()
#     patient = Patient(first_name=patient_data['first_name'],
#                       last_name=patient['last_name'],
#                       address=patient_data['address'],
#                       date_of_birth = patient_data['age'])
    
#     db_session.add(patient)
#     db_session.commit()

