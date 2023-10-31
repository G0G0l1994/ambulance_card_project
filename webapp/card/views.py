from flask import render_template, flash, redirect, url_for, request, session
from flask import Blueprint
from webapp.card.forms import CardForm
from webapp.patient.forms import NewPatient
from webapp.card.models import CardOne
from webapp.db import db_session
import psycopg2

conn = psycopg2.connect(user="vqklygsa", password='5C42T__du4u1BsNdcbgU9e5P8jNmpGyk', host='cornelius.db.elephantsql.com', port='5432')

blueprint = Blueprint('card', __name__, url_prefix='/cards')

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  title = "Карта"
  newform = CardOne()
  con = request.form
  print(con)
  keys = con.keys()
  columns = ','.join(keys)
  values = ','.join(['%({})s'.format(k) for k in keys])
  cursor = conn.cursor()
  insert = 'insert into Card_one ({0}) values ({1})'.format(columns, values)
  print(cursor.mogrify(insert, con), "Готово по бд")
  print(form.jaundice.data)
  """ newform.complaint = form.complaints.data
  newform.anamnesis = form.anamnesis.data
  newform.general_assessment = form.general_assessment.data
  newform.сonsciousness = form.сonsciousness.data
  newform.glasgow_scale = form.glazgow_scale.data
  newform.body_position = form.body_position.data
  newform.temperature = form.t_body.data
  newform.respiratory_rate = form.respiratory_rate.data
  newform.saturation = form.oxygen_saturation.data
  
  db_session.add(newform)
  db_session.commit() """
  
  print("Сохранено")
  flash("Сохранено")
  return render_template('main_card.html',page_title = title, form_general=form)

""" 
@blueprint.route('/process-card')
def process_card():
  if "anamnesis" in session:
    anamnesis = session['anamnesis']
    return f"<h1>{anamnesis}</h1>"
"""
""" 
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
  skin_color = Skin(color_skin = form_skin.skin_colour.data)
  skin_yellownes = Skin(jaundice = form_skin.skin_yellowness.data)
  skin_rash = Skin(rash = form_skin.skin_rash.data)
  skin_throat = Skin(throat = form_skin.skin_throat.data)
  skin_tonsils = Skin(tonsils = form_skin.skin_tonsils.data)
  lymph_nodes = Skin(lymph_nodes = form_skin.skin_lymph_nodes.data)
  swelling = Skin(swelling = form_skin.skin_swelling.data)
  db_session.add_all([skin_dryness, skin_color, skin_yellownes, skin_rash, skin_throat, skin_tonsils, lymph_nodes, swelling])
  db_session.commit()
  print("Готово")
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin)


@blueprint.route('/breathing_system', methods=["GET", "POST"])
def breath():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  respiratory_type = RespiratorySystem(respiratory_type = form_breath.respiratory_type.data)
  wheezing = RespiratorySystem(wheezing = form_breath.breath_wheezing.data)
  wheezing_localisation = RespiratorySystem(wheezing_localisation = form_breath.breath_wheezing_localisation.data)
  dyspnea = RespiratorySystem(dyspnea = form_breath.breath_dyspnea.data)
  db_session.add_all([respiratory_type, wheezing, wheezing_localisation, dyspnea])
  db_session.commit()
  print("Готово")
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath)

@blueprint.route('/heart')
def heart():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  heart_sounds = CardiovascularSystem(heart_sounds = form_heart.heart_sounds.data)
  heart_sounds_type = CardiovascularSystem(heart_sounds_type = form_heart.heart_sounds_type)
  heart_murmur = CardiovascularSystem(heart_murmur = form_heart.heart_murmur.data)
  pulse = CardiovascularSystem(pulse = form_heart.heart_pulse.data)
  heart_rate_deficit = CardiovascularSystem(heart_rate_deficit = form_heart.heart_rate_deficit.data)
  heart_accent_tone = CardiovascularSystem(heart_tone_accent = form_heart.heart_accent_tone)
  
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart)

@blueprint.route('/digestion')
def digestion():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  form_digestion = DisgestionSystem()
  abdominal_condition = DigestiveSystem(stomach = form_digestion.abdominal_condition.data)
  peritoneal_irritation_symptoms = DigestiveSystem(peritoneal_irritation_symptoms = form_digestion.peritoneal_irritation_symptoms.data)
  liver = DigestiveSystem(liver = form_digestion.liver.data)
  stool_type = DigestiveSystem(stool_type = form_digestion.stool_type.data)
  stool_frequence_general = DigestiveSystem(stool_frequence_general = form_digestion.stool_frequence_general.data)
  stool_frequence_specific = DigestiveSystem(form_digestion.stool_frequence_specific.data)
  db_session.add_all([abdominal_condition, peritoneal_irritation_symptoms,liver, stool_type, stool_frequence_general, stool_frequence_specific])
  db_session.commit()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart, form_digestion = form_digestion)

@blueprint.route('/nerves')
def nerves():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  form_digestion = DisgestionSystem()
  form_nerves = NervousSystemForm()
  behaviour = NervousSystem(behaviour = form_nerves.behaviour.data)
  meningial_symptoms = NervousSystem(meningial_symptoms = form_nerves.meningial_symptoms.data)
  reaction_to_light = NervousSystem(reaction_to_light = form_nerves.reaction_to_light.data)
  pupils = NervousSystem(pupils_of_the_eyes = form_nerves.pupils.data)
  anisocoria = NervousSystem(anisocoria = form_nerves.anisocoria.data)
  nystagmus = NervousSystem(nystagmus = form_nerves.nystagmus.data)
  focal_signs = NervousSystem(focal_signs = form_nerves.focal_signs.data)
  speech = NervousSystem(speech = form_nerves.speech.data)
  paralysis = NervousSystem(paralysis = form_nerves.paralysis.data)
  sensitivity = NervousSystem(sensitivity = form_nerves.sensitivity.data)
  db_session.add_all([behaviour, meningial_symptoms, reaction_to_light, pupils, anisocoria, nystagmus, focal_signs, speech, paralysis, sensitivity])
  db_session.commit()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart, form_digestion = form_digestion, form_nerves = form_nerves)

@blueprint.route('/urogenital')
def urogenital():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  form_digestion = DisgestionSystem()
  form_nerves = NervousSystemForm()
  form_urogenital = UrogentitalSystem()
  urination = GenitourinarySystem(urination = form_urogenital.urination.data)
  urine = GenitourinarySystem(urine = form_urogenital.urine.data)
  kidney_punch = GenitourinarySystem(kidney_punch = form_urogenital.pounding_symptom.data)
  db_session.add_all([urination, urine, kidney_punch])
  db_session.commit()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart, form_digestion = form_digestion, form_nerves = form_nerves,  form_urogenital = form_urogenital)

@blueprint.route('/local_status')
def status_localis():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  form_digestion = DisgestionSystem()
  form_nerves = NervousSystemForm()
  form_urogenital = UrogentitalSystem()
  form_status_localis = StatusLocalisForm()
  form_diagnosis = DiagnosisForm()
  status_localis = StatusLocalis(status_localis = form_status_localis.status_localis.data)
  db_session.add(status_localis)
  db_session.commit()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart, form_digestion = form_digestion, form_nerves = form_nerves,  form_urogenital = form_urogenital, form_status_localis = form_status_localis)

@blueprint.route("/aid")
def aid():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  form_digestion = DisgestionSystem()
  form_nerves = NervousSystemForm()
  form_urogenital = UrogentitalSystem()
  form_status_localis = StatusLocalisForm()
  form_aid = AidForm()
  
  ecg_before_aid = ECG(ECG_before = form_aid.ecg_before_aid.data)
  ecg_after_aid = ECG(ECG_after = form_aid.ecg_after_aid.data)
  aid_provided = AID(aid = form_aid.aid_provided.data)
  t_body_after_aid = IndicatorsAfter(temperature = form_aid.t_body_after_aid.data)
  respiratory_rate = IndicatorsAfter(respiratory_rate = form_aid.respiratory_rate_after_aid.data)
  oxygen_saturation_after_aid = IndicatorsAfter(saturation = form_aid.oxygen_saturation_after_aid.data)
  heart_rate_after_aid = IndicatorsAfter(heartbite = form_aid.heart_rate_after_aid.data)
  pulse_after_aid = IndicatorsAfter(pulse = form_aid.pulse_after_aid.data)
  blood_glucose_after_aid = IndicatorsAfter(blood_glucose = form_aid.blood_glucose_after_aid.data)
  db_session.add_all([ecg_before_aid, ecg_after_aid, aid_provided, t_body_after_aid, respiratory_rate, oxygen_saturation_after_aid, heart_rate_after_aid, pulse_after_aid, blood_glucose_after_aid])
  db_session.commit()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart, form_digestion = form_digestion, form_nerves = form_nerves,  form_urogenital = form_urogenital, form_status_localis = form_status_localis, form_aid = form_aid)

@blueprint.route('/diagnosis')
def diagnosis():
  form_general = CardFormGeneral()
  form_skin = SkinForm()
  form_breath = BreathingSysthem()
  form_heart = HeartForm()
  form_digestion = DisgestionSystem()
  form_nerves = NervousSystemForm()
  form_urogenital = UrogentitalSystem()
  form_diagnosis = DiagnosisForm()
  diagnosis = Diagnosis(diagnosis = form_diagnosis.diagnosis.data)
  db_session.add(diagnosis)
  db_session.commit()
  return render_template('main_card.html', form_general=form_general, form_skin = form_skin, form_breath = form_breath, form_heart = form_heart, form_digestion = form_digestion, form_nerves = form_nerves,  form_urogenital = form_urogenital, form_diagnosis = form_diagnosis) """