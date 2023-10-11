from db import db_session
from webapp.user.models import Doctors
from getpass import getpass
from werkzeug.security import generate_password_hash

doctor = Doctors(id_table = 2, first_name = "Olga", last_name = "Ivanova", username = "Olga_new_11")
password = getpass("Введите пароль")
doctor.set_password(password)
db_session.add(doctor)
db_session.commit()
print("Добавлен")
