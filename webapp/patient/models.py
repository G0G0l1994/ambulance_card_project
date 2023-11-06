from sqlalchemy import Column, Integer, String, Date
from webapp.db import Base




class Patient(Base):
    __tablename__ = "patient"
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    surname = Column(String)
    address = Column(String)
    date_of_birth = Column(Date)
    
    

    def __repr__(self):
        return f"Patient {self.id} {self.first_name} {self.last_name}"

