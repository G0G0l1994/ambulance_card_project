from flask import render_template, url_for,redirect
from flask import Blueprint
from datetime import datetime
from webapp.patient.forms import NewPatient, Time
from flask import request

blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

@blueprint.route('/create', methods=['POST','GET'])
def create():
  title = "Новый пациент"
  patient_form = NewPatient()
  dtn = datetime.now().strftime("%H:%M")
  if request.method == 'POST':
    return render_template('patient.html', page_title=title, form=patient_form,current_time=dtn)
  
  return render_template("patient.html",page_title=title, form=patient_form)




# @blueprint.route("/set-time", methods=["POST","GET"])
# def set_datetime():
    
#     else:
         
    
