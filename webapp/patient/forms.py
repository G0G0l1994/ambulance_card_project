from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField
from wtforms.validators import DataRequired
from webapp.patient.create_patient import create_patient

class NewPatient(FlaskForm):
    patient = create_patient()
    first_name = patient['first_name']
    first_name_field = StringField("Имя", validators=[DataRequired()],default=patient['first_name'], render_kw={"class": "form-control"})
    last_name = patient['last_name']
    last_name_field = StringField("Фамилия", validators=[DataRequired()], render_kw={"class": "form-control"})
    surname = patient['surname']
    surname_field = StringField("Отчество", validators=[DataRequired()], render_kw={"class": "form-control"})
    age = patient['age']
    age_field = StringField("Дата рождения", validators=[DataRequired()], render_kw={"class": "form-control"})
    address = patient['address']
    address_field = StringField("Адрес", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Заполнить карту вызова", render_kw={"class": "btn btn-primary"})


