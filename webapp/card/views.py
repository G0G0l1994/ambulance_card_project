from flask import render_template, flash, redirect, url_for
from flask import Blueprint
from webapp.card.forms import CardFormGeneral, SkinForm
from webapp.patient.forms import NewPatient
from webapp.card.models import Complaint, Anamnesis, GeneralAssessment, IndicatorsBefore, Skin
from webapp.db import db_session


blueprint = Blueprint('card', __name__, url_prefix='/cards')

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin)

@blueprint.route('/general', methods=["GET", 'POST'])
def general():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  anamnesis = Anamnesis(anamnesis=form_general.anamnesis.data)
  print(anamnesis)
  db_session.add(anamnesis)
  db_session.commit()
  general_assesment = GeneralAssessment(general_assessment=form_general.condition.data)
  db_session.add(general_assesment)
  db_session.commit()
  conscience = GeneralAssessment(сonsciousness = form_general.conscience.data)
  db_session.add(conscience)
  db_session.commit()
  glazgow_scale = GeneralAssessment(glasgow_scale = form_general.glazgow_scale.data)
  body_position = GeneralAssessment(body_position = form_general.body_position.data)
  temperature = IndicatorsBefore(temperature = form_general.t_body.data)
  respiratory_rate = IndicatorsBefore(respiratory_rate = form_general.respiratory_rate.data)
  oxygen_saturation = IndicatorsBefore(saturation = form_general.oxygen_saturation.data)
  heart_rate = IndicatorsBefore(heartbite = form_general.heart_rate.data)
  pulse = IndicatorsBefore(pulse = form_general.pulse.data)
  pressure_systolic = IndicatorsBefore(blood_pressure_systolic = form_general.pressure_systolic.data)
  pressure_diastolic = IndicatorsBefore(blood_pressure_diastolic = form_general.pressure_diastolic.data)
  blood_glucose = IndicatorsBefore(blood_glucose = form_general.blood_glucose.data)
  db_session.add_all([glazgow_scale, body_position, temperature, respiratory_rate, oxygen_saturation, heart_rate, pulse, pressure_systolic, pressure_diastolic, blood_glucose])
  db_session.commit()
  flash("Сохранено")
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin)

@blueprint.route('/skin', methods=["GET", 'POST'])
def skin():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  skin_dryness = Skin(dry_skin = form_skin.skin_dryness.data)
  db_session.add(skin_dryness)
  db_session.commit()
  print("Готово")
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin)
