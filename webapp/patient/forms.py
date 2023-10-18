from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField
from wtforms.validators import DataRequired
from webapp.patient.create_patient import create_patient

class NewPatient(FlaskForm):
    patient = create_patient()
    first_name = StringField("Имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name = StringField("Фамилия", validators=[DataRequired()], render_kw={"class": "form-control"})
    surname = StringField("Отчество", validators=[DataRequired()], render_kw={"class": "form-control"})
    age = StringField("Дата рождения", validators=[DataRequired()], render_kw={"class": "form-control"})
    address = StringField("Адрес", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Заполнить карту вызова", render_kw={"class": "btn btn-primary"})


