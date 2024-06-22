import sys
from datetime import datetime

from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from flask import Blueprint

from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import Users
from webapp.card.forms import CardForm
from webapp.card.models import CardOne
from webapp.db import Base, db_session
from webapp.utilits import data_dict,save_doctor, save_patient



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
    user = Users.query.filter(Users.username == form.username.data).first()
    sys.stdout.flush()
    print(f'Результат работы функции check_password: {user.check_password(password)}')
    if user and user.check_password(password):
      login_user(user, remember=form.remember_me.data) #запоминание пользователя
      print("Уcпех")
      flash("Вы успешно вошли на сайт")
      print(f"ID пользователя: {current_user.id}, {current_user.role}")
      save_doctor(data_dict=data_dict)
      if current_user.role == "Врач":
        return redirect(url_for('user.main'))
      elif current_user.role == "Админ":
        return redirect(url_for("user.main"))
      else:
        return redirect(url_for("user.main_dispatcher"))
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
  if  not current_user.is_authenticated:
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('registration.html', page_title=title, form=form)
  print(f"ID текущего доктора: {current_user.id}")
  return redirect(url_for('user.login'))
  

@blueprint.route('/register', methods=["POST", "GET"])
def process_reg():
  form = RegistrationForm()
  if form.validate_on_submit():
    new_user = Users(username=form.username.data, first_name=form.name.data, last_name=form.lastname.data, role=form.role.data, surname = form.surname.data)
    new_user.set_password(form.password.data)
    db_session.add(new_user)
    db_session.commit()
    flash("Вы зарегистрировались!")
    
    return redirect(url_for('user.login'))
  flash("Исправьте ошибки в форме")
  return redirect(url_for('user.register'))

@blueprint.route('/dispatcher/new_card', methods=["POST","GET"])
def new_card():
  current_time=datetime.now().strftime("%H:%M")
  form = CardForm(current_time=current_time)
  if request.method == "POST":
    form.save_card(request)
    return redirect(url_for("user.main_dispatcher"))
  return render_template("dispatcher.html", form = form)
  
  

@blueprint.route('/dispatcher/main', methods=["POST","GET"])
def main_dispatcher():
  data_card = CardOne.query.filter(CardOne.status == "Принят").all()
  form = CardForm()
  data = []
  for card in data_card:
      print(card)
      join = [card.last_name,card.first_name,card.surname,card.status, card.crew]
      data.append(join)
  if request.method == "POST":
    return redirect(url_for('user.new_card'))
  elif request.method == "GET":
    print("GET")
    print(data)
    return render_template("dispatcher_main.html", data=data, form = form)

# def card_process():
#   card = CardForm()



