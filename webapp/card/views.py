from flask import render_template,redirect,url_for,request
from flask import Blueprint
from webapp.models import DiagnosisCode
from webapp.card.forms import CardForm
from webapp.patient.models import Patient
from webapp.card.models import CardOne

from webapp.config import conn
from webapp.utilits import save_card,update_time,data_dict, remove_data_dict
from psycopg2 import Error

my_cur = conn.cursor()

blueprint = Blueprint('card', __name__, url_prefix='/cards')

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  title = "Карта"
  mkb_code =  DiagnosisCode.query.all()
  if request.method == "POST":
    mkb = request.form.get('mkb')
    save_card(table_name="card_united", conn=conn,data_dict=data_dict)
  return render_template('main_card.html',page_title = title, form_general=form, mkb_code=mkb_code)

@blueprint.route('/finished_card', methods=["GET", 'POST'])
def finished_card():
  my_cur.execute("SELECT * FROM card_united WHERE id IN (SELECT MAX(id) FROM card_united)")
  data = my_cur.fetchall()
  print(data)
  my_cur.execute("SELECT * FROM Users WHERE id = (SELECT doctor_id FROM card_united ORDER BY id DESC LIMIT 1)")
  data_doctor = my_cur.fetchall()
  my_cur.execute("SELECT * FROM patient WHERE id = (SELECT patient_id FROM card_united ORDER BY id DESC LIMIT 1)")
  data_patient = my_cur.fetchall()
  if request.method=="POST":
    remove_data_dict(data_dict=data_dict)
    print("на главной")
    return redirect(url_for("user.main"))
  return render_template('finished_card.html', data=data, data_doctor=data_doctor, data_patient = data_patient)

@blueprint.route("/update_time", methods=["GET", 'POST'])
def update():
  if request.method=="POST":
    update_time("card_united", conn=conn,data_dict=data_dict)
    return redirect(url_for("card.finished_card"))
  else:
    return redirect(url_for("patient.create"))

@blueprint.route("/history",methods=["GET",'POST'])
def history():
  data = CardOne.query.filter(CardOne.doctor_id == data_dict['doctor_id']).all()
  patient_data = []
  if request.method == "GET":
    print(len(data))
    for i in data:
      qu = Patient.query.filter(Patient.id == i.patient_id).first()
      if qu == None:
        continue
      else:
        print(qu.last_name, qu.date_of_birth)
    return render_template("main.html", data = data)
  return render_template('main.html', data=data)
  