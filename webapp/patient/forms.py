from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TextAreaField, SelectField, IntegerField, FloatField, IntegerRangeField
from wtforms.validators import DataRequired
from webapp.patient.create_patient import create_patient

class NewPatient(FlaskForm):
    patient = create_patient()
    first_name = StringField("Имя", validators=[DataRequired()],default=patient['first_name'], render_kw={"class": "form-control"})
    last_name = StringField("Фамилия", validators=[DataRequired()], render_kw={"class": "form-control"})
    surname = StringField("Отчество", validators=[DataRequired()], render_kw={"class": "form-control"})
    age = StringField("Дата рождения", validators=[DataRequired()], render_kw={"class": "form-control"})
    address = StringField("Адрес", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Заполнить карту вызова", render_kw={"class": "btn btn-primary"})


class PatientForm(FlaskForm):
    complaints = TextAreaField("Жалобы", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Жалобы пациента..."})
    anamnesis = TextAreaField("Анамнез", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Анамнез..."})
