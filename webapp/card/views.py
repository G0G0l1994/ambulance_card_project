from flask import render_template, flash, redirect, url_for, request, session
from flask import Blueprint
from webapp.card.forms import CardForm
from webapp.patient.forms import NewPatient
from webapp.card.models import CardOne
from webapp.db import db_session
from webapp.utilits import save_card
import psycopg2
from psycopg2 import Error
from webapp.config import time_dict

conn = psycopg2.connect(user="vqklygsa", password='5C42T__du4u1BsNdcbgU9e5P8jNmpGyk', host='cornelius.db.elephantsql.com', port='5432')

blueprint = Blueprint('card', __name__, url_prefix='/cards')


@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  title = "Карта"
  print(form.validate_on_submit())
  save_card(form,table_name="card_united", conn=conn,time_dict=time_dict)
  return render_template('main_card.html',page_title = title, form_general=form)
