from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, Text, ForeignKey
from webapp.db import Base, engine


class CardOne(Base):
    __tablename__ = "Card_one"
    
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
    
    complaint = Column(Text)
    anamnesis = Column(Text)
    general_assessment = Column(String())
    сonsciousness = Column(String()) #сознание
    glasgow_scale = Column(Integer) #шкала Глазго
    body_position = Column(String()) # положение тела
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
    dry_skin = Column (String())
    color_skin = Column(String)
    jaundice = Column(String()) #желтушность
    rash = Column(String()) #сыпь
    throat = Column(String()) #зев
    tonsils = Column(String())#миндалины
    lymph_nodes = Column(String()) #лимфоузлы
    swelling = Column(String()) #отёки
    
    #breathing system
    respiratory_type = Column(String())
    wheezing = Column(String())# хрипы
    wheezing_localisation = Column(String())# хрипы
    dyspnea = Column(String()) #одышка
    
    #cardiovascular system
    heart_rate_deficit = Column(Boolean)
    heart_tone_accent = Column(Boolean) #акцент тона
    rhythmic_tone = Column(Boolean)
    arrhythmic_tone = Column(Boolean)
    clear = Column(Boolean)
    muffled = Column(Boolean)# глухие тоны
    muted = Column(Boolean)# приглушенные
    none_sounds = Column(Boolean) #отсутствуют
    none_murmur = Column(Boolean)
    systolic = Column(Boolean)
    diastolic = Column(Boolean)
    pericardial_friction_rub = Column(Boolean)
    rhythmic_pulse = Column(Boolean)
    arrhythmic_pulse = Column(Boolean)
    weak = Column(Boolean)
    thready = Column(Boolean)# нитевидный
    tense = Column(Boolean)# напряжённый
    non_pulse = Column(Boolean)
    
    #abdominal
    liver = Column(String()) # печень
    frequency_of_bowel_movement = Column(String())# частота стула
    abdomens_soft = Column(Boolean)
    painless_stomach = Column(Boolean)
    pain_stomach = Column(Boolean)
    tense = Column(Boolean) #напряжённый
    swollen = Column(Boolean) # вздут
    involved_in_the_act_of_breathing = Column(Boolean)
    formed_stool = Column(Boolean) #оформленый стул
    thin_stool = Column(Boolean) #разжижен
    unformed_stool = Column(Boolean) #жидкий
    regular_stool = Column(Boolean)
    irregular_stool = Column(Boolean)
    is_shchetkin_blumberg = Column(Boolean)
    is_voskresensky = Column(Boolean)
    is_ortner = Column(Boolean)
    is_rovzinga = Column(Boolean)
    is_pasternatsky = Column(Boolean)
    is_sitkovsky = Column(Boolean)
    is_obraztsova = Column(Boolean)
    is_murphy = Column(Boolean)
    
    #nervous system
    behavior = Column(String())
    reaction_to_light = Column(String())
    pupils_of_the_eyes = Column(String())
    anisocoria = Column(Boolean)
    nystagmus = Column(Boolean)
    focal_sings = Column(Boolean)
    speech = Column(String())
    none_symptoms = Column(Boolean)
    nuchal_rigidity = Column(Boolean)
    is_kernig_symptom = Column(Boolean)
    is_brudzinski_symptom = Column(Boolean)
    none_paralysis = Column(Boolean)
    left = Column(Boolean)
    right = Column(Boolean)
    saved = Column(Boolean)
    missing_sens = Column(Boolean)
    reduced = Column(Boolean)
    left_sens = Column(Boolean)
    right_sens = Column(Boolean)
    
    #urogenital ssytem
    kidney_punch = Column(String) #симптом покалачивания
    urine = Column(String)
    painless = Column(Boolean)
    free = Column(Boolean)
    painful_urine = Column(Boolean)
    difficult = Column(Boolean)
    missing_urine = Column(Boolean)
    light_yellow = Column(Boolean)
    cloudy = Column(Boolean)
    with_inclusions = Column(Boolean)
    with_sediment = Column(Boolean)
    
    #local status
    status_localis = Column(Text)
    
    
    #aid
    ecg_before = Column(Text)
    ecg_after = Column(Text)
    aid = Column(Text)
    temperature_after = Column(Float)
    respiratory_rate_after = Column(Integer)
    heartbite_after = Column(Integer)
    saturation_after = Column(Integer)
    pulse_after = Column(Integer)
    blood_pressure_systolic_after = Column(Integer)
    blood_pressure_diastolic_after = Column(Integer)
    blood_glucose_after = Column(Float)
    diagnosis = Column(String)
    
Base.metadata.create_all(bind=engine)