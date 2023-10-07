from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#class LoginForm(FlaskForm):
  #username = StringField("Ник", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш ник"})
  #name = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваше имя"})
  #surname = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваша фамилия"})
  #password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш пароль"})
  #password_2 = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Повторите пароль"})
  #submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})


class LoginForm(FlaskForm):
  username = StringField("Ник", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш ник"})
  password_entry = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Ваш пароль"})
  submit = SubmitField("Войти!", render_kw={"class": "btn btn-primary"})