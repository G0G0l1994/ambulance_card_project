import os
from dotenv import load_dotenv

from datetime import timedelta
import psycopg2

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
REMEMBER_COOKIE_DURATION = timedelta(days=2)
SQLALCHEMY_TRACK_MODIFICATION = False
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
conn = psycopg2.connect(user=os.getenv('user'), password=os.getenv('password'), host=os.getenv('host'), port=os.getenv('port'))
