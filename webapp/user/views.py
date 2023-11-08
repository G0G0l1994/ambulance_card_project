from flask import flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask import Blueprint
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import doctors
from webapp.db import Base, db_session
from webapp.config import data_dict
import sys

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login', methods=['POST', "GET"])
def login():
  title = "Войти"
  login_form = LoginForm()
  return render_template('login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
  form = LoginForm()
  if form.validate_on_submit():
    password = form.password_entry.data
    user = doctors.query.filter(doctors.username == form.username.data).first()
    sys.stdout.flush()
    print(f'Результат работы функции check_password: {user.check_password(password)}')
    if user and user.check_password(password):
      login_user(user, remember=form.remember_me.data) #запоминание пользователя
      print("Уcпех")
      flash("Вы успешно вошли на сайт")
      print(f"ID текущего доктора: {current_user.id}")
      return redirect(url_for('user.main'))
  print("Ошибка")
  flash("Неправильное имя пользователя или пароль")
  return redirect(url_for('user.login'))

@blueprint.route('/main')
def main():
  return render_template('main.html')

@blueprint.route('/logout')
def logout():
  flash("Вы разлогинились")
  logout_user()
  return redirect(url_for('user.login'))

@blueprint.route('/register')
def register():
  if current_user.is_authenticated:
    print(f"ID текущего доктора: {current_user.id}")
    return redirect(url_for('user.login'))
  form = RegistrationForm()
  title = "Регистрация"
  return render_template('registration.html', page_title=title, form=form)

@blueprint.route('/register', methods=["POST", "GET"])
def process_reg():
  form = RegistrationForm()
  if form.validate_on_submit():
    new_user = doctors(username=form.username.data, first_name=form.name.data, last_name=form.surname.data)
    new_user.set_password(form.password.data)
    db_session.add(new_user)
    db_session.commit()
    flash("Вы зарегистрировались!")
    print(f"ID текущего доктора: {current_user.id}")
    return redirect(url_for('user.login'))
  flash("Исправьте ошибки в форме")
  return redirect(url_for('user.register'))

