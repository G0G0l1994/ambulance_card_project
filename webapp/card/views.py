from flask import render_template,redirect,url_for,request
from flask import Blueprint
from webapp.card.forms import CardForm

from webapp.config import conn
from webapp.utilits import save_card, save_doctor,update_time,data_dict
from psycopg2 import Error

my_cur = conn.cursor()

blueprint = Blueprint('card', __name__, url_prefix='/cards')

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  title = "Карта"
  save_card(table_name="card_united", conn=conn,data_dict=data_dict)
  save_doctor(data_dict=data_dict)
  return render_template('main_card.html',page_title = title, form_general=form)

@blueprint.route('/finished_card')
def finished_card():
  my_cur.execute("SELECT * FROM card_united WHERE id IN (SELECT MAX(id) FROM card_united)")
  data = my_cur.fetchall()
  my_cur.execute("SELECT * FROM doctors WHERE id = (SELECT doctor_id FROM card_united ORDER BY id DESC LIMIT 1)")
  data_doctor = my_cur.fetchall()
  my_cur.execute("SELECT * FROM patient WHERE id = (SELECT patient_id FROM card_united ORDER BY id DESC LIMIT 1)")
  data_patient = my_cur.fetchall()
  return render_template('finished_card.html', data=data, data_doctor=data_doctor, data_patient = data_patient)

@blueprint.route("/update_time", methods=["GET", 'POST'])
def update():
  if request.method=="POST":
    update_time("card_united", conn=conn,data_dict=data_dict)
    return redirect(url_for("card.finished_card"))
  else:
    return redirect(url_for("patient.create"))
  