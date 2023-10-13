
from flask import flash, render_template, redirect, url_for
from flask_login import login_user, logout_user
from flask import Blueprint
from webapp.user.forms import LoginForm
from webapp.models import Doctors
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
  return redirect(url_for('main'))