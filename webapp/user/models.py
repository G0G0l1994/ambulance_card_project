from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String
from webapp.models import Base
from flask_login import UserMixin

class Users(Base, UserMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String())
    surname = Column(String())
    last_name = Column(String())
    username = Column(String(), unique = True)
    role = Column(String())
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
        return f"User: {self.id}, {self.username}, {self.role}"
