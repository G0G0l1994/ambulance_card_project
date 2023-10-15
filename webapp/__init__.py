from flask import Flask, render_template, flash, redirect, url_for
from webapp.user.forms import LoginForm, PatienForm
from flask_login import LoginManager
from webapp.user.models import Doctors
from webapp.db import Base, engine, db_session
from webapp.user.views import blueprint as user_blueprint
import logging

logging.basicConfig( 
    filename = "mylog.log", level=logging.DEBUG
    )

def create_app():
  app = Flask(__name__, template_folder="templates", static_folder="static")
  app.config.from_pyfile("config.py")

  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = "user.login"
  app.register_blueprint(user_blueprint)
  
  @login_manager.user_loader
  def load_user(user_id):
    return Doctors.query.get(user_id)
  

  
  #@app.route('/registration')
  #def index():
  # title = "Регистрация"
  #  register_form = LoginForm()
  #  return render_template('registration.html', page_title=title, form=register_form)
  
  return app