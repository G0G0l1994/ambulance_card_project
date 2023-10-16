from flask import render_template
from flask import Blueprint


from webapp.patient.forms import NewPatient


blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

@blueprint.route('/create', methods=['POST', "GET"])
def create():
  title = "Новый пациент"
  patient_form = NewPatient()
  return render_template('patient.html', page_title=title, form=patient_form)


    
    