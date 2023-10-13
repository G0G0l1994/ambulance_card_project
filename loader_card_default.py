from webapp.db import db_session
from datetime import date, datetime
from webapp.models import *

def default_card():
    card = Card(
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
    
    general_assessment = GeneralAssessment(id_table=9,
                                           general_assessment="удовлетворительно",
                                           сonsciousness="ясное",
                                           glasgow_scale=15, 
                                           body_position="активное")
    db_session.add(general_assessment)
    
    indicators_before = IndicatorsBefore(id_table=8,temperature=36.0,
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
    
    skin = Skin(id_table=10,
                dry_skin="сухие",
                color_skin="обычной окраски",
                jaundice="нет",
                rash="нет",
                throat="спокоен",
                tonsils="не увеличены",
                lymph_nodes="не увеличены",
                swelling="нет")
    db_session.add(skin)
    
    respiratory_system = RespiratorySystem(id_table=11,
                                           respiratory_type="везикулярное",
                                           wheezing="нет",
                                           dyspnea="нет")
    db_session.add(respiratory_system)
    
    cardiovascular_system = CardiovascularSystem(id_table=12,)
    db_session.commit()

default_card()