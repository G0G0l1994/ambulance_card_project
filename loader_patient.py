from webapp.db import db_session
from webapp.models import Patient
from webapp.create_patient import Create_patient

def save_patient():
    patient_dict = Create_patient()
    patient = Patient(first_name=patient_dict['first_name'],
                      last_name=patient_dict['last_name'],
                      address=patient_dict['address'],
                      id_table=3)
    db_session.add(patient)
    db_session.commit()
    print(f"Пациент {patient_dict['first_name']} добавлен")

save_patient()
