from flask import flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask import Blueprint
from webapp.user.forms import LoginForm, PatienForm, RegistrationForm
from webapp.user.models import Doctors
from webapp.db import Base, db_session
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
    user = Doctors.query.filter(Doctors.username == form.username.data).first()
    sys.stdout.flush()
    print(f'Результат работы функции check_password: {user.check_password(password)}')
    if user and user.check_password(password):
      login_user(user, remember=form.remember_me.data) #запоминание пользователя
      print("Уcпех")
      flash("Вы успешно вошли на сайт")
      return redirect(url_for('user.page1'))
  print("Ошибка")
  flash("Неправильное имя пользователя или пароль")
  return redirect(url_for('user.login'))
@blueprint.route('/page1')
def page1():
  return render_template('page1.html')

@blueprint.route('/logout')
def logout():
  flash("Вы разлогинились")
  logout_user()
  return redirect(url_for('user.main'))

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = PatienForm()
  return render_template('main_card.html', form=form)

@blueprint.route('/register')
def register():
  if current_user.is_authenticated:
    return redirect(url_for('user.page1'))
  form = RegistrationForm()
  title = "Регистрация"
  return render_template('registration.html', page_title=title, form=form)

@blueprint.route('/register', methods=["POST", "GET"])
def process_reg():
  form = RegistrationForm()
  if form.validate_on_submit():
    new_user = Doctors(username=form.username.data, first_name=form.name.data, last_name=form.surname.data)
    new_user.set_password(form.password.data)
    db_session.add(new_user)
    db_session.commit()
    flash("Вы зарегистрировались!")
    return redirect(url_for('user.page1'))
  flash("Исправьте ошибки в форме")
  return redirect(url_for('user.register'))
