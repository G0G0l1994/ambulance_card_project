from flask import render_template, url_for,redirect
from flask import Blueprint
from webapp.card.forms import *

blueprint = Blueprint('card', __name__,url_prefix="/card")



@blueprint.route('/main_card', methods=["GET", 'POST'])
def main_card():
  form = PatientForm()
  return render_template('main_card.html', form=form)
