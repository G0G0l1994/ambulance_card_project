from faker import Faker
from flask import request
from datetime import datetime
from flask_login import current_user
import psycopg2
from psycopg2 import Error
from webapp.patient.models import Patient
from webapp.db import db_session




def create_patient():
    """Генерирует данные пациента, моделируя действия диспетчера службы СМП

    Returns:
        dict: Any
    """
    patient = Faker("ru_RU")
    patient_data = patient.name().split()
    return {'first_name': patient_data[1],
            'surname': patient_data[2],
            'last_name': patient_data[0],
            'date_of_birth': patient.date_of_birth(minimum_age=18, maximum_age=70),
            'address': patient.street_address()
            }

def add_time(index: any ,time_dict: dict) -> dict:
    """
    Добавляет время в словаря для сохранения и использования на front-end
    Args:
        index (str): index from front-end
        time_dict (dict): dict for save time

    Returns:
        dict: saved time
    """
    time_dict[index] = datetime.now().strftime("%H:%M")
    print(time_dict)
    return time_dict


def save_card(form, table_name,conn, data_dict={}):
    """
    Сохранение в БД
    [Args]:
    form : wtf.form
    table_name : table_name from DB
    conn : connect for DB
    """
    try:
        con = request.form
        cursor = conn.cursor()
        keys = list(con.keys())+list(data_dict.keys())
        print(keys)
        values = list(con.values())+list(data_dict.values())
        print(values)
        columns = ', '.join(keys)
        placeholders = ', '.join(['%s' for _ in range(len(keys))])
        insert_query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        cursor.execute(insert_query, values)
        conn.commit()
        print(cursor.mogrify(insert_query, values), "Готово добавление в БД")
    except psycopg2.DatabaseError as error:
        conn.rollback()
        print("Error: ", error)

def save_doctor(data_dict):
    current_doctor = current_user.id 
    data_dict['doctor_id'] = current_doctor
    print("Доктор сохранен")
    return data_dict

def save_patient(patient_form,data_dict):
    
    """сохранение пациента в БД

    Args:
        patient_form (wtf.form): Any
    """
    current_patient = Patient.query.filter(Patient.last_name == patient_form.last_name.data).first()
    if current_patient:
        print(current_patient)
        data_dict['patient_id'] = current_patient.id
        return data_dict
    else:
        patient = Patient(first_name = patient_form.first_name.data,
                            last_name = patient_form.last_name.data,
                            surname = patient_form.surname.data,
                            address = patient_form.address.data,
                            date_of_birth = patient_form.date_of_birth.data)
        db_session.add(patient)
        db_session.commit()
        current_patient = Patient.query.filter(Patient.last_name == patient_form.last_name.data).first()
        print(f"{patient} сохранён")
        data_dict['patient_id'] = current_patient.id
        return data_dict

