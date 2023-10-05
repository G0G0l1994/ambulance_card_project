from sqlalchemy import Column, Integer, String, DATE, DateTime, Float, Boolean
from db import Base, engine

#-------------------Основные сущности-------------------
class Doctors(Base):
    __tablename__ = "Врач"
    
    id_table = Column(Integer)
    id_doctor = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    username = Column(String(), unique = True)
    password = Column(String(),unique = True)
    
    def __repr__(self):
        return f"Doctor {self.id_doctor}, {self.username}"


class Patient(Base):
    __tablename__ = "Пациент"
    
    id_table = Column(Integer)
    id_patient = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    adress = Column(String())

    def __repr__(self):
        return f"Пациент {self.id_patient} {self.first_name} {self.last_name}"
    
    
class Card(Base):
    __tablename__ = "Карта"
    
    id_table = Column(Integer)
    id_patient = Column(Integer)
    id_doctor = Column(Integer)
    id_card = Column(Integer, primary_key = True)
    date_card = Column(DATE) # дата карты
    time_of_receipt = Column(DateTime) # время приёма
    transmission_time = Column(DateTime) # время передачи
    departure_time = Column(DateTime) #время выезда бригады
    arrival_time = Column(DateTime) #время прибытия
    start_time_of_hospitalization = Column(DateTime) #время начала госпитализации
    time_of_arrival_at_hospital = Column(DateTime) #время прибытия в больницу
    call_end_time = Column(DateTime) # время окончания вызова
    
    
class Patient_Card_History(Base):
    __tablename__ = "История пациента"
    
    id_table = Column(Integer)
    id_patient = Column(Integer)
    id_card = Column(Integer)
    date_card = Column(DATE)


class Doctor_Card_History(Base):
    __tablename__ = "История вызовов врача"

    id_table = Column(Integer)
    id_card = Column(Integer)
    id_doctor = Column(Integer)

#-------------------Раздел составных частей карт-------------------

class Complaint(Base): #Жалобы
    __tablename__ = "Жалобы"
    
    id_table = Column(Integer)
    id_card = Column(Integer)
    сomplaint = Column(String())
    

class Anamnesis(Base): #Анамнез
    __tablename__ = "Анамнез"
    
    id_table = Column(Integer)
    id_card = Column(Integer)
    anamnesis = Column(String())


class General_Assessment(Base): #Общие данные
    __tablename__ = "Общие данные"
    
    id_table = Column(Integer)
    id_card = Column(Integer)
    
    general_assessment = Column(String())
    сonsciousness = Column(String()) #сознание
    glasgow_scale = Column(Integer) #шкала Глазго
    body_position = Column(String()) # положение тела


class Indicators_before(Base): #показатели до оказания помощи
    __tablename__ = "Показатели до оказания помощи"
    
    id_card = Column(Integer)
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
    __tablename__ = "Кожные покровы"
    
    id_card = Column(Integer)
    id_table = Column(Integer)
    dry_skin = Column (String())
    color_skin = Column(String)
    jaundice = Column(String()) #желтушность
    rash = Column(String()) #сыпь
    throat = Column(String()) #зев
    tonsils = Column(String())#миндалины
    lymph_nodes = Column(String()) #лимфоузлы
    swelling = Column(String()) #отёки


class  Respiratory_system(Base):
    __tablename__ = "Дыхательная система"
    
    id_card = Column(Integer)
    id_table = Column(Integer)
    respiratory_type = Column(String())
    wheezing = Column(String())# хрипы
    dyspnea = Column(String()) #одышка
    
    
class Cardiovascular_System(Base):
    __tablename__ = "Сердечно-сосудистая система"
    
    id_card = Column(Integer)
    id_table = Column(Integer)
    heart_sounds = Column(String()) #тоны сердца
    heart_murmur = Column(String()) #шум сердца
    pulse_characteristic = Column(String())
    heart_rate_deficit = Column(Boolean)
    heart_tone_accent = Column(Boolean) #акцент тона
    
    

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)