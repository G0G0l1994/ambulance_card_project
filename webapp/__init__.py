from flask import Flask, render_template, flash, redirect, url_for
from webapp.forms import LoginForm
from flask_login import LoginManager, login_user, logout_user
from webapp.models import db,Doctors


def create_app():
  app = Flask(__name__, template_folder="templates", static_folder="static")
  app.config.from_pyfile("config.py")
  db.init_app(app)

  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = "login"
  
  @login_manager.user_loader
  def load_user(user_id):
    return Doctors.query.get(user_id)
  
  @app.route('/')
  def main():
    return render_template('main.html')
  
  #@app.route('/index')
  #def index():
  # title = "Регистрация"
  #  register_form = LoginForm()
  #  return render_template('index.html', page_title=title, form=register_form)
  
  @app.route('/login', methods=['POST'])
  def login():
    title = "Войти"
    login_form = LoginForm()
    return render_template('try.html', page_title=title, form=login_form)

  @app.route('/process-login', methods=['POST'])
  def process_login():
    form = LoginForm()
    if form.validate_on_submit():
      user = Doctors.query.filter(Doctors.username == form.username.data).first()
      if user in None:
        print("None")
      else:
        print(user)
      if user and user.check_password(form.password.data):
        login_user(user)
        flash("Вы успешно вошли на сайт")
        return redirect(url_for('main'))
    else:
      print("Ошибка")
      flash("Неправильное имя пользователя или пароль")
      return redirect(url_for('login'))
  
  @app.route('/logout')
  def logout():
    flash("Вы разлогинились")
    logout_user()
    return redirect(url_for('main'))
  
  return app