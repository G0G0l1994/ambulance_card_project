from flask import render_template, flash
from flask import Blueprint
from webapp.card.forms import CardFormGeneral
from webapp.patient.forms import NewPatient
from webapp.card.models import Complaint, Anamnesis, GeneralAssessment
from webapp.db import db_session


blueprint = Blueprint('patient', __name__, url_prefix='/new_patient')

@blueprint.route('/create', methods=['POST', "GET"])
def create():
  title = "Новый пациент"
  patient_form = NewPatient()
  return render_template('patient.html', page_title=title, form=patient_form)

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardFormGeneral()
  return render_template('main_card.html', form=form)

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card_forms():
  form = CardFormGeneral()
  if form.validate_on_submit():
    anamnesis = Anamnesis(anamnesis=form.anamnesis.data)
    db_session.add(anamnesis)
    db_session.commit()
    complaint = Complaint(complaint=form.complaints.data)
    db_session.add(complaint)
    db_session.commit()
    flash("Отправлено")