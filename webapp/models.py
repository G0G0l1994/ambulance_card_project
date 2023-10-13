
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Boolean, Text, ForeignKey
from webapp.db import Base, engine
from flask_login import UserMixin

#-------------------Основные сущности-------------------

class Doctors(Base, UserMixin):
    __tablename__ = "Doctors"
    
    id_table = Column(Integer)
    id = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    username = Column(String(), unique = True)
    password = Column(String())
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        print(f'результат работы функции set_password{self.password}')
    
    def check_password(self, password):
        print(f'Селф {self.password}')
        print(f'Введенный пароль{password}')
        print(f'Результат проверки функции {check_password_hash(self.password, password)}')
        return check_password_hash(self.password, password)
    def __repr__(self):
        return f"Doctor {self.id}, {self.username}"

class Patient(Base):
    __tablename__ = "Patient"
    
    id_table = Column(Integer)
    id = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    adress = Column(String())

    def __repr__(self):
        return f"Patient {self.id_patient} {self.first_name} {self.last_name}"
    
    
class Card(Base):
    __tablename__ = "Card"
    
    id_table = Column(Integer)
    id_patient = Column(Integer, ForeignKey(Patient.id), index=True)
    id_doctor = Column(Integer,ForeignKey(Doctors.id), index=True)
    id = Column(Integer, primary_key = True)
    date_card = Column(Date) # дата карты
    time_of_receipt = Column(DateTime) # время приёма
    transmission_time = Column(DateTime) # время передачи
    departure_time = Column(DateTime) #время выезда бригады
    arrival_time = Column(DateTime) #время прибытия
    start_time_of_hospitalization = Column(DateTime) #время начала госпитализации
    time_of_arrival_at_hospital = Column(DateTime) #время прибытия в больницу
    call_end_time = Column(DateTime) # время окончания вызова
    
    
class PatientCardHistory(Base):
    __tablename__ = "Patient_Card_History"
    
    id = Column(Integer, primary_key = True)
    id_table = Column(Integer)
    id_patient = Column(Integer, ForeignKey(Patient.id), index=True)
    id_card = Column(Integer,ForeignKey(Card.id), index=True)
    date_card = Column(Date)


class DoctorCardHistory(Base):
    __tablename__ = "Doctor_Card_History"
    
    id = Column(Integer, primary_key = True)
    id_table = Column(Integer)
    id_card = Column(Integer,ForeignKey(Card.id), index=True)
    id_doctor = Column(Integer,ForeignKey(Doctors.id), index=True)

#-------------------Раздел составных частей карт-------------------

class Complaint(Base): #Жалобы
    __tablename__ = "Complaint"
    
    id = Column(Integer, primary_key = True)
    id_table = Column(Integer)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    сomplaint = Column(Text)
    

class Anamnesis(Base): #Анамнез
    __tablename__ = "Anamnesis"
    
    id = Column(Integer, primary_key = True)
    id_table = Column(Integer)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    anamnesis = Column(Text)


class GeneralAssessment(Base): #Общие данные
    __tablename__ = "General_Assessment"
    
    id = Column(Integer, primary_key = True)
    id_table = Column(Integer)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    
    general_assessment = Column(String())
    сonsciousness = Column(String()) #сознание
    glasgow_scale = Column(Integer) #шкала Глазго
    body_position = Column(String()) # положение тела


class IndicatorsBefore(Base): #показатели до оказания помощи
    __tablename__ = "Indicators_before"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    temperature = Column(Float)
    respiratory_rate = Column(Integer)
    heartbite = Column(Integer)
    saturation = Column(Integer)
    pulse = Column(Integer)
    blood_pressure = Column(String()) # подумать как привести к int"/"int
    normal_blood_pressure = Column(String()) # подумать как привести к int"/"int
    blood_glucose = Column(Float)


class Skin(Base):
    __tablename__ = "Skin"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    dry_skin = Column (String())
    color_skin = Column(String)
    jaundice = Column(String()) #желтушность
    rash = Column(String()) #сыпь
    throat = Column(String()) #зев
    tonsils = Column(String())#миндалины
    lymph_nodes = Column(String()) #лимфоузлы
    swelling = Column(String()) #отёки


class  RespiratorySystem(Base):
    __tablename__ = "Respiratory_System"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    respiratory_type = Column(String())
    wheezing = Column(String())# хрипы
    dyspnea = Column(String()) #одышка
    
    
class CardiovascularSystem(Base):
    __tablename__ = "Cardiovascular_System"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    heart_sounds = Column(String()) #тоны сердца
    heart_murmur = Column(String()) #шум сердца
    pulse_characteristic = Column(String())
    heart_rate_deficit = Column(Boolean)
    heart_tone_accent = Column(Boolean) #акцент тона

class DigestiveSystem(Base):
    __tablename__ = "Digestive_System"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    stomach = Column(String())
    symptoms_of_peritoneal_irritation = Column(String())# симптомы раздражения брюшины, возможно вынести в свою таблицу
    liver = Column(String()) # печень
    bowel_movement = Column(String()) #стул 
    frequency_of_bowel_movement = Column(String()) # частота стула

class NervousSystem(Base):
    __tablename__ = "Nervous_System"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    behavior = Column(String())
    meningeal_symptoms = Column(String())
    reaction_to_light = Column(String())
    pupils_of_the_eyes = Column(String())
    anisocoria = Column(Boolean)
    nystagmus = Column(Boolean)
    focal_sings = Column(Boolean)
    speech = Column(String())
    paralysis = Column(String()) # возможно в отдельную
    sensitivity = Column(String()) # возможно в отдельную

class GenitourinarySystem(Base):
    __tablename__ = "Genitourinary_System"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    urination = Column(String) #возможно в отдельную
    kidney_punch = Column(String) #симптом покалачивания
    urine = Column(String)

class StatusLocalis(Base):
    __tablename__ = "Status_Localis"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    status_localis = Column(Text)
    
class ECG(Base):
    __tablename__ = "ECG" #ЭКГ
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)    
    ECG_before = Column(Text)
    ECG_after = Column(Text)
    
class AID(Base):
    __tablename__ = "AID"
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    aid = Column(Text)

class IndicatorsAfter(Base): #показатели после оказания помощи
    __tablename__ = "Indicators_after"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    temperature = Column(Float)
    respiratory_rate = Column(Integer)
    heartbite = Column(Integer)
    saturation = Column(Integer)
    pulse = Column(Integer)
    blood_pressure = Column(String()) # подумать как привести к int"/"int
    blood_glucose = Column(Float)
 
class Diagnosis(Base):
    __tablename__ = "Diagnosis"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    diagnosis = Column(String)


Base.metadata.create_all(bind=engine)