from flask import render_template,redirect,url_for,request
from flask import Blueprint
from webapp.card.forms import CardForm


from webapp.utilits import save_card, save_doctor,update_data
import psycopg2
from psycopg2 import Error
from webapp.config import data_dict, form_dict

conn = psycopg2.connect(user="vqklygsa", password='5C42T__du4u1BsNdcbgU9e5P8jNmpGyk', host='cornelius.db.elephantsql.com', port='5432')
my_cur = conn.cursor()

blueprint = Blueprint('card', __name__, url_prefix='/cards')


@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  title = "Карта"
  print(form.validate_on_submit())
  save_card(table_name="card_united", conn=conn,data_dict=data_dict)
  save_doctor(data_dict=data_dict)
  
  return render_template('main_card.html',page_title = title, form_general=form)

@blueprint.route('/finished_card')
def finished_card():
  my_cur.execute("SELECT * FROM card_united WHERE id IN (SELECT MAX(id) FROM card_united)")
  data = my_cur.fetchall()
  return render_template('finished_card.html', data=data)

@blueprint.route("/update_card", methods=["GET", 'POST'])
def update_card():
  update_data(table_name="card_united", conn=conn,data_dict=data_dict,form_dict=form_dict)
  return redirect(url_for("card.finished_card"))
  