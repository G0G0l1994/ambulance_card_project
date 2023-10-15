from webapp.db import db_session
from datetime import date, datetime
from webapp.models import *
from webapp.create_patient import Create_patient

def default_card():
    patient_dict = Create_patient()
    patient = Patient(first_name=patient_dict['first_name'],
                      last_name=patient_dict['last_name'],
                      address=patient_dict['address'],
                      date_of_birth = patient_dict['age'],
                      id_table=3)
    
    db_session.add(patient)
    db_session.commit()
    card = Card(id_patient = Patient.id,
                date_card=date.today(),
                time_of_receipt=datetime.now(),
                transmission_time=datetime.now(),
                departure_time=datetime.now(),
                arrival_time=datetime.now(),
                start_time_of_hospitalization=None,
                time_of_arrival_at_hospital=None,
                call_end_time=datetime.now())
    db_session.add(card)
    
    complaint = Complaint(id_table=6,сomplaint="введите жалобы")
    db_session.add(complaint)
    
    anamnesis = Anamnesis(id_table=7,anamnesis="введите анамнез")
    db_session.add(anamnesis)
    
    general_assessment = GeneralAssessment(general_assessment="удовлетворительно",
                                           сonsciousness="ясное",
                                           glasgow_scale=15, 
                                           body_position="активное")
    db_session.add(general_assessment)
    
    indicators_before = IndicatorsBefore(temperature=36.0,
                                         respiratory_rate=16,
                                         heartbite=70,
                                         saturation=98,
                                         pulse=70,
                                         blood_pressure_systolic=120,
                                         blood_pressure_diastolic=80,
                                         normal_blood_pressure_systolic=120,
                                         normal_blood_pressure_diastolic=80,
                                         blood_glucose=3.3)
    db_session.add(indicators_before)
    
    skin = Skin(dry_skin="сухие",
                color_skin="обычной окраски",
                jaundice="нет",
                rash="нет",
                throat="спокоен",
                tonsils="не увеличены",
                lymph_nodes="не увеличены",
                swelling="нет")
    db_session.add(skin)
    
    respiratory_system = RespiratorySystem(respiratory_type="везикулярное",
                                           wheezing="нет",
                                           dyspnea="нет")
    db_session.add(respiratory_system)
    db_session.commit()

default_card()