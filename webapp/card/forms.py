from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class PatientForm(FlaskForm):
    complaints = TextAreaField("Жалобы", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Жалобы пациента..."})
    anamnesis = TextAreaField("Анамнез", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Анамнез..."})
