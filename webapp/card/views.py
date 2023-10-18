from flask import render_template, flash, redirect, url_for
from flask import Blueprint
from webapp.card.forms import CardForm
from webapp.patient.forms import NewPatient
from webapp.card.models import Complaint, Anamnesis, GeneralAssessment
from webapp.db import db_session


blueprint = Blueprint('card', __name__, url_prefix='/cards')

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  return render_template('main_card.html', form=form)

@blueprint.route('/process_card', methods=["GET", 'POST'])
def process_card():
  form = CardForm()
  anamnesis = Anamnesis(anamnesis=form.anamnesis.data)
  print(anamnesis)
  db_session.add(anamnesis)
  db_session.commit()
  general_assesment = GeneralAssessment(general_assessment=form.condition.data)
  db_session.add(general_assesment)
  db_session.commit()
  return redirect(url_for('card.main_card'))