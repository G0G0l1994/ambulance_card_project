from flask import Flask, render_template, flash, redirect
from webapp.forms import LoginForm

def create_app():
  app = Flask(__name__, template_folder="templates")
  app.config.from_pyfile("config.py")
  
  @app.route('/index')
  def index():
    title = "Регистрация"
    register_form = LoginForm()
    return render_template('index.html', page_title=title, form=register_form)
  
  @app.route('/login')
  def login():
    title = "Войти"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

  return app