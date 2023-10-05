from webapp.db import db_session
from webapp.models import Doctors

doctor = Doctors(id_table = 2, first_name = "Olga", last_name = "Ivanova", password = "1234567120", username = "Olga_new")
db_session.add(doctor)
db_session.commit()