from flask import render_template, flash
from flask import Blueprint
from webapp.card.forms import CardForm
from webapp.patient.forms import NewPatient, Time
from webapp.card.models import Complaint, Anamnesis, GeneralAssessment
from webapp.db import db_session

from datetime import datetime
from webapp.patient.forms import NewPatient, Time
from webapp.card.forms import CardForm
from webapp.card.models import Complaint, Anamnesis
from flask import request


blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

time_dict={"time_of_receipt": datetime.now().strftime("%H:%M"),
           "transmission_time": datetime.now().strftime("%H:%M"),
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
  title = "Пациент"
  patient_form = NewPatient()
  time_form = Time()
  if request.method == 'POST':
    index = request.form["index"]
    add_time(index,time_dict)
    return render_template("patient.html",page_title=title, form=patient_form, time_form = time_form, time = time_dict)
  else:
    return render_template("patient.html",page_title=title, form=patient_form, time_form = time_form, time = time_dict )

# @blueprint.route('/main_card', methods=["GET", 'POST'])
# def main_card():
#   form = CardFormGeneral()
#   return render_template('main_card.html', form=form)

# @blueprint.route('/main_card', methods=["GET", 'POST'])
# def main_card_forms():
#   form = CardFormGeneral()
#   if form.validate_on_submit():
#     anamnesis = Anamnesis(anamnesis=form.anamnesis.data)
#     db_session.add(anamnesis)
#     db_session.commit()
#     complaint = Complaint(complaint=form.complaints.data)
#     db_session.add(complaint)
#     db_session.commit()
#     flash("Отправлено")

         
    
