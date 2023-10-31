from flask import render_template, flash, redirect, url_for, request, session
from flask import Blueprint
from webapp.card.forms import CardForm
from webapp.patient.forms import NewPatient
from webapp.card.models import CardOne
from webapp.db import db_session
import psycopg2
from psycopg2 import Error

conn = psycopg2.connect(user="vqklygsa", password='5C42T__du4u1BsNdcbgU9e5P8jNmpGyk', host='cornelius.db.elephantsql.com', port='5432')

blueprint = Blueprint('card', __name__, url_prefix='/cards')

@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = CardForm()
  title = "Карта"
  print(form.validate_on_submit())
  try:
    if request.method == "POST":
      con = request.form
      cursor = conn.cursor()
      keys = list(con.keys())
      print(keys)
      values = list(con.values())
      print(values)
      columns = ', '.join(keys)
      placeholders = ', '.join(['%s' for _ in range(len(keys))])
      insert_query = f'INSERT INTO card_united ({columns}) VALUES ({placeholders})'
      cursor.execute(insert_query, values)
      conn.commit()
      print(cursor.mogrify(insert_query, values), "Готово по бд")
      print(form.jaundice.data)
  except psycopg2.DatabaseError as error:
    print("Error: ", error)
  return render_template('main_card.html',page_title = title, form_general=form)