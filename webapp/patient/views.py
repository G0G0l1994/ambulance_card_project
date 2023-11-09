from flask import render_template
from flask import Blueprint
from webapp.patient.forms import NewPatient, Time
from webapp.utilits import add_time,save_patient,data_dict
from webapp.patient.forms import NewPatient, Time
from flask import request


blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

@blueprint.route('/create', methods=['POST','GET'])
def create():
  title = "Пациент"
  time_form = Time()
  patient_form = NewPatient()
  if request.method == 'POST':
    index = request.form["index"]
    add_time(index,data_dict)
    return render_template("patient.html",page_title=title, 
                           form=patient_form, time_form = time_form, 
                           time = data_dict)
  else:
    save_patient(patient_form,data_dict)
    return render_template("patient.html",page_title=title, 
                           form=patient_form, time_form = time_form, 
                           time = data_dict)

         
    
