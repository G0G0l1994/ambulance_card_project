from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired
from webapp.patient.create_patient import create_patient
from datetime import datetime

class NewPatient(FlaskForm):
    patient = create_patient()
    first_name = StringField("Имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name = StringField("Фамилия", validators=[DataRequired()], render_kw={"class": "form-control"})
    surname = StringField("Отчество", validators=[DataRequired()], render_kw={"class": "form-control"})
    age = StringField("Дата рождения", validators=[DataRequired()], render_kw={"class": "form-control"})
    address = StringField("Адрес", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Заполнить карту вызова", render_kw={"class": "btn btn-primary", "color" : "red"})

class Time(FlaskForm):
    current_time=datetime.now().strftime("%H:%M")
    time_of_receipt =  DateTimeField("Время приёма", format = "%H:%M")
    transmission_time = DateTimeField("Время передачи", format = "%H:%M")
    departure_time = DateTimeField("Время принятия вызова", format = "%H:%M")
    arrival_time = DateTimeField("Время прибытия", format = "%H:%M")
    start_time_of_hospitalization = DateTimeField("Время начала госпитализации", format = "%H:%M")
    time_of_arrival_at_hospital = DateTimeField("Время прибытия в стационар", format = "%H:%M")
    call_end_time = DateTimeField("Окончание вызова", format = "%H:%M")
    
    
    
#     transmission_time =  # время передачи
#     departure_time =  #время выезда бригады
#     arrival_time =  #время прибытия
#     start_time_of_hospitalization =  #время начала госпитализации
#     time_of_arrival_at_hospital =  #время прибытия в больницу
#     call_end_time =  # время окончания вызова
