from flask import Flask, render_template

def create_app():
  app = Flask(__name__)
  
  @app.route('/')
  def index():
    title = "Главная страница"
    return render_template('index.html', page_title=title)