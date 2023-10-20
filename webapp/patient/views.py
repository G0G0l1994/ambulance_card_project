from flask import render_template, url_for,redirect
from flask import Blueprint
from datetime import datetime
from webapp.patient.forms import NewPatient, Time
from flask import request

blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

time_dict={"time_of_receipt": None,
           "transmission_time": None,
           "departure_time": None,
           "arrival_time" : None,
           "start_time_of_hospitalization" : None,
           "time_of_arrival_at_hospital": None,
           "call_end_time" : None}

def add_time(index,time_dict):
  time_dict[index] = datetime.now().strftime("%H:%M")
  print(time_dict)
  return time_dict

@blueprint.route('/create', methods=['POST','GET'])
def create():
  title = "Новый пациент"
  patient_form = NewPatient()
  time_form = Time()
  if request.method == 'POST':
    index = request.form["index"]
    add_time(index,time_dict)
    return render_template("patient.html",page_title=title, form=patient_form, time_form = time_form, time = time_dict)
  else:
    return render_template("patient.html",page_title=title, form=patient_form, time_form = time_form, time = time_dict )


         
    
