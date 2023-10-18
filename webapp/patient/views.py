from flask import render_template, url_for,redirect
from flask import Blueprint
<<<<<<< HEAD
from webapp.user.views import main
=======
from webapp.patient.forms import PatientForm
>>>>>>> development

from webapp.patient.forms import NewPatient


blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

@blueprint.route('/create', methods=['POST', "GET"])
def create():
  title = "Новый пациент"
  patient_form = NewPatient()
  return render_template('patient.html', page_title=title, form=patient_form)
<<<<<<< HEAD
=======

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = PatientForm()
  return render_template('main_card.html', form=form)

    
    
>>>>>>> development
