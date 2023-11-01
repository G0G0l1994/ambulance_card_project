from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, Text
from webapp.db import Base, engine

class CardOne(Base):
    __tablename__ = "card_united"
    
    id = Column(Integer, primary_key = True)
    patient_id = Column(Integer,  index=True)
    doctor_id = Column(Integer, index=True)
    #время
    date_card = Column(Date) # дата карты
    time_of_receipt = Column(Time) # время приёма
    transmission_time = Column(Time) # время передачи
    departure_time = Column(Time) #время выезда бригады
    arrival_time = Column(Time) #время прибытия
    start_time_of_hospitalization = Column(Time) #время начала госпитализации
    time_of_arrival_at_hospital = Column(Time) #время прибытия в больницу
    call_end_time = Column(Time) # время окончания вызова
    #общие сведения
    zhaloby = Column(Text)
    anamnesis = Column(Text)
    general_assessment = Column(String)
    сonsciousness = Column(String) #сознание
    glasgow_scale = Column(Integer) #шкала Глазго
    body_position = Column(String) # положение тела
    #показатели до 
    temperature_before = Column(Float)
    respiratory_rate_before = Column(Integer)
    heartbite_before = Column(Integer)
    saturation_before = Column(Integer)
    pulse_before = Column(Integer)
    blood_pressure_systolic_before = Column(Integer)
    blood_pressure_diastolic_before = Column(Integer)
    normal_blood_pressure_systolic = Column(Integer) 
    normal_blood_pressure_diastolic = Column(Integer)
    blood_glucose_before = Column(Float)
    #кожные покровы
    dry_skin = Column (String)
    color_skin = Column(String)
    jaundice = Column(String) #желтушность
    rash = Column(String) #сыпь
    throat = Column(String) #зев
    tonsils = Column(String)#миндалины
    lymph_nodes = Column(String) #лимфоузлы
    swelling = Column(String) #отёки
    #дыхательная система
    respiratory_type = Column(String)
    wheezing = Column(String)# хрипы
    wheezing_localisation = Column(String)# хрипы
    dyspnea = Column(String) #одышка
    heart_rate_deficit = Column(Boolean)
    heart_tone_accent = Column(String) #акцент тона
    rhythmic_tone = Column(String)
    tone_of_heart=Column(String)
    murmur = Column(String)
    rhythmic_pulse = Column(String)
    characteristic_pulse = Column(String)
    #живот
    liver = Column(String) # печень   
    pain_stomach = Column(String)
    characteristic_stomach = Column(String)
    involved_in_the_act_of_breathing = Column(Boolean)
    formed_type_stool = Column(String)
    regular_stool = Column(String)
    rate_stool = Column(Integer)
    is_shchetkin_blumberg = Column(Boolean)
    is_voskresensky = Column(Boolean)
    is_ortner = Column(Boolean)
    is_rovzinga = Column(Boolean)
    is_pasternatsky = Column(Boolean)
    is_sitkovsky = Column(Boolean)
    is_obraztsova = Column(Boolean)
    is_murphy = Column(Boolean)
    #нервная система
    behaviour = Column(String)
    reaction_to_light = Column(String)
    pupils_of_the_eyes = Column(String)
    anisocoria = Column(Boolean)
    nystagmus = Column(Boolean)
    focal_signs = Column(Boolean)
    speech = Column(String)
    none_symptoms = Column(Boolean)
    nuchal_rigidity = Column(Boolean)
    is_kernig_symptom = Column(Boolean)
    is_brudzinski_symptom = Column(Boolean)
    paralysis = Column(String)
    sensitive = Column(String)
    #мочеполовая система
    kidney_punch = Column(String) #симптом покалачивания
    characteristic_urine = Column(String)
    characteristic_urination = Column(String)
    #статус локалис
    status_localis = Column(Text)
    #ЭКГ
    ecg_before = Column(Text)
    ecg_after = Column(Text)
    #помощь
    aid = Column(Text)
    #показатели после
    temperature_after = Column(Float)
    respiratory_rate_after = Column(Integer)
    heartbite_after = Column(Integer)
    saturation_after = Column(Integer)
    pulse_after = Column(Integer)
    blood_pressure_systolic_after = Column(Integer)
    blood_pressure_diastolic_after = Column(Integer)
    blood_glucose_after = Column(Float)
    #диагноз
    diagnosis = Column(String)
    submit = Column(Boolean)


Base.metadata.create_all(bind=engine)