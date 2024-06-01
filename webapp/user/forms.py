from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired, EqualTo, InputRequired


class RegistrationForm(FlaskForm):
  username = StringField("Ник", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваше имя пользователя"})
  name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваше имя"})
  surname = StringField("Отчество", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Ваше отчество"})
  lastname = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваша фамилия"})
  role = RadioField("Должность", validate_choice=[InputRequired()], choices=[("Врач","Врач"),("Диспетчер","Диспетчер")], default="Врач", render_kw={"class":"form-check-label", "style":"list-style-type:none"})
  password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш пароль"})
  password_2 = PasswordField("Пароль", validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control", "placeholder" : "Повторите пароль"})
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})


class LoginForm(FlaskForm):
  username = StringField("Ник", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш ник"})
  password_entry = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш пароль"})
  remember_me = BooleanField("Запомнить меня", default=True, render_kw={'class': "form-check-input"})
  submit = SubmitField("Войти!", render_kw={"class": "btn btn-primary"})
  
