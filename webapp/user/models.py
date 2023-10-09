from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, DATE, DateTime, Float, Boolean, Text
from webapp.models import Base
from flask_login import UserMixin

class Doctors(Base, UserMixin):
    __tablename__ = "Doctors"
    
    id_table = Column(Integer)
    id_doctor = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    username = Column(String(), unique = True)
    password = Column(String())
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return f"Doctor {self.id_doctor}, {self.username}"
