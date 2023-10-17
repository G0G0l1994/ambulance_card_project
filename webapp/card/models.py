from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, Text, ForeignKey
from webapp.db import Base, engine 

class Card(Base):
    __tablename__ = "Card"
    
    id = Column(Integer, primary_key = True)
    patient_id = Column(Integer,  index=True)
    doctor_id = Column(Integer, index=True)
    
    date_card = Column(Date) # дата карты
    time_of_receipt = Column(Time) # время приёма
    transmission_time = Column(Time) # время передачи
    departure_time = Column(Time) #время выезда бригады
    arrival_time = Column(Time) #время прибытия
    start_time_of_hospitalization = Column(Time) #время начала госпитализации
    time_of_arrival_at_hospital = Column(Time) #время прибытия в больницу
    call_end_time = Column(Time) # время окончания вызова

class Complaint(Base): #Жалобы
    __tablename__ = "Complaint"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, ForeignKey(Card.id), index=True)
    
    сomplaint = Column(Text)
    

class Anamnesis(Base): #Анамнез
    __tablename__ = "Anamnesis"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer, index=True)
    
    anamnesis = Column(Text)


class GeneralAssessment(Base): #Общие данные
    __tablename__ = "General_Assessment"
    
    id = Column(Integer, primary_key = True)
    id_card = Column(Integer,  index=True)
    
    general_assessment = Column(String())
    сonsciousness = Column(String()) #сознание
    glasgow_scale = Column(Integer) #шкала Глазго
    body_position = Column(String()) # положение тела


class IndicatorsBefore(Base): #показатели до оказания помощи
    __tablename__ = "Indicators_before"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer,  index=True)
    
    temperature = Column(Float)
    respiratory_rate = Column(Integer)
    heartbite = Column(Integer)
    saturation = Column(Integer)
    pulse = Column(Integer)
    blood_pressure_systolic = Column(Integer)
    blood_pressure_diastolic = Column(Integer)
    normal_blood_pressure_systolic = Column(Integer) 
    normal_blood_pressure_diastolic = Column(Integer)
    blood_glucose = Column(Float)


class Skin(Base):
    __tablename__ = "Skin"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    
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
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    
    respiratory_type = Column(String())
    wheezing = Column(String())# хрипы
    dyspnea = Column(String()) #одышка
    
    
class CardiovascularSystem(Base):
    __tablename__ = "Cardiovascular_System"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    heart_rate_deficit = Column(Boolean)
    heart_tone_accent = Column(Boolean) #акцент тона

class HeartSounds(Base):
    __tablename__= "Heart_sounds"
    
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    rhythmic = Column(Boolean)
    arrhythmic = Column(Boolean)
    clear = Column(Boolean)
    muffled = Column(Boolean)# глухие тоны
    muted = Column(Boolean)# приглушенные
    none_sounds = Column(Boolean) #отсутствуют

class HeartMurmur(Base):
    __tablename__ = "Heart_murmur"
    
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    none_murmur = Column(Boolean)
    systolic = Column(Boolean)
    diastolic = Column(Boolean)
    pericardial_friction_rub = Column(Boolean)
    
class PulseCharacteristic(Base):
    __tablename__ = "Pulse_characteristic"
    
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    rhythmic = Column(Boolean)
    arrhythmic = Column(Boolean)
    weak = Column(Boolean)
    thready = Column(Boolean)# нитевидный
    tense = Column(Boolean)# напряжённый
    non_pulse = Column(Boolean)

class DigestiveSystem(Base):
    __tablename__ = "Digestive_System"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    liver = Column(String()) # печень
    frequency_of_bowel_movement = Column(String()) # частота стула
    
class Stomach(Base):
    __tablename__ = "Stomach"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    abdomens_soft = Column(Boolean)
    painless = Column(Boolean)
    pain = Column(Boolean)
    tense = Column(Boolean) #напряжённый
    swollen = Column(Boolean) # вздут
    involved_in_the_act_of_breathing = Column(Boolean)
    
class BowelMovement(Base):
    __tablename__ = "Bowel_movement"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    formed_stool = Column(Boolean) #оформленый стул
    thin_stool = Column(Boolean) #разжижен
    unformed_stool = Column(Boolean) #жидкий
    regular = Column(Boolean)
    irregular = Column(Boolean)
    
    
class AbdominalSymptoms(Base):
    __tablename__ = "Abdominal_symptoms"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    Shchetkin_Blumberg = Column(Boolean)
    Voskresensky = Column(Boolean)
    Ortner = Column(Boolean)
    Rovzinga = Column(Boolean)
    Pasternatsky = Column(Boolean)
    Sitkovsky = Column(Boolean)
    Obraztsova = Column(Boolean)
    Murphy = Column(Boolean)
    
class NervousSystem(Base):
    __tablename__ = "Nervous_System"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    behavior = Column(String())
    reaction_to_light = Column(String())
    pupils_of_the_eyes = Column(String())
    anisocoria = Column(Boolean)
    nystagmus = Column(Boolean)
    focal_sings = Column(Boolean)
    speech = Column(String())


class MeningealSymptoms(Base):
    __tablename__ = "Meningeal_symptoms"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    none_symptoms = Column(Boolean)
    nuchal_rigidity = Column(Boolean)
    Kernig_symptom = Column(Boolean)
    Brudzinski_symptom = Column(Boolean)

class Paralysis(Base):
    __tablename__ = "Paralysis"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    none_paralysis = Column(Boolean)
    left = Column(Boolean)
    right = Column(Boolean)
    
class Sensitivity(Base):
    __tablename__ = "Sensitivity"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    saved = Column(Boolean)
    missing = Column(Boolean)
    reduced = Column(Boolean)
    left = Column(Boolean)
    right = Column(Boolean)
    
class GenitourinarySystem(Base):
    __tablename__ = "Genitourinary_System"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    kidney_punch = Column(String) #симптом покалачивания
    urine = Column(String)

class Urination(Base):
    __tablename__ = "Urination"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    painless = Column(Boolean)
    free = Column(Boolean)
    painful = Column(Boolean)
    difficult = Column(Boolean)
    missing = Column(Boolean)

class Urine(Base):
    __tablename__ = "Urine"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    light_yellow = Column(Boolean)
    cloudy = Column(Boolean)
    with_inclusions = Column(Boolean)
    with_sediment = Column(Boolean)


class StatusLocalis(Base):
    __tablename__ = "Status_Localis"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    status_localis = Column(Text)
    
    
class ECG(Base):
    __tablename__ = "ECG" #ЭКГ
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)    
    ECG_before = Column(Text)
    ECG_after = Column(Text)
    
class AID(Base):
    __tablename__ = "AID"

    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    aid = Column(Text)

class IndicatorsAfter(Base): #показатели после оказания помощи
    __tablename__ = "Indicators_after"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    
    temperature = Column(Float)
    respiratory_rate = Column(Integer)
    heartbite = Column(Integer)
    saturation = Column(Integer)
    pulse = Column(Integer)
    blood_pressure_systolic = Column(Integer)
    blood_pressure_diastolic = Column(Integer)
    blood_glucose = Column(Float)
 
class Diagnosis(Base):
    __tablename__ = "Diagnosis"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, ForeignKey(Card.id), index=True)
    id_table = Column(Integer)
    diagnosis = Column(String)