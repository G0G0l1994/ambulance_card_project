from flask import render_template, flash,redirect,url_for
from flask import Blueprint
from webapp.card.forms import CardForm
from webapp.patient.forms import NewPatient, Time
from webapp.db import db_session
from webapp.config import time_dict
from webapp.utilits import add_time
from datetime import datetime
from webapp.patient.forms import NewPatient, Time
from webapp.card.forms import CardForm
from webapp.utilits import save_patient
from flask import request
import psycopg2


blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')


# time_dict={"time_of_receipt": datetime.now().strftime("%H:%M"),
#            "transmission_time": datetime.now().strftime("%H:%M"),
#            "departure_time": None,
#            "arrival_time" : None,
#            "start_time_of_hospitalization" : None,
#            "time_of_arrival_at_hospital": None,
#            "call_end_time" : None}


@blueprint.route('/create', methods=['POST','GET'])
def create():
  title = "Пациент"
  time_form = Time()
  patient_form = NewPatient()
  if request.method == 'POST':
    index = request.form["index"]
    add_time(index,time_dict)
    return render_template("patient.html",page_title=title, form=patient_form, time_form = time_form, time = time_dict)
  else:
    save_patient(patient_form)
    return render_template("patient.html",page_title=title, form=patient_form, time_form = time_form, time = time_dict)

         
    
