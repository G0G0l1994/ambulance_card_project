from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, Text, ForeignKey
from webapp.db import Base, engine 

#-------------------Основные сущности-------------------

class PatientCardHistory(Base):
    __tablename__ = "Patient_Card_History"
    
    id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, index=True)
    card_id = Column(Integer, index=True)
    date_card = Column(Date)


class DoctorCardHistory(Base):
    __tablename__ = "Doctor_Card_History"
    
    id = Column(Integer, primary_key = True)
    card_id = Column(Integer, index=True)
    doctor_id = Column(Integer, index=True)

#-------------------Раздел составных частей карт-------------------


