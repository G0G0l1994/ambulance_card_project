# import os
# from dotenv import load_dotenv

from datetime import timedelta
import psycopg2

# load_dotenv()

# SECRET_KEY = os.environ.get("SECRET_KEY")
# REMEMBER_COOKIE_DURATION = timedelta(days=2)
# SQLALCHEMY_TRACK_MODIFICATION = False
# SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
# conn = psycopg2.connect(user=os.getenv('user'), password=os.getenv('password'), host=os.getenv('host'), port=os.getenv('port'))

SECRET_KEY = "ewfrejugjrtgbjrtbtrhnbnrtbnttbtjgijitgejv nrjergegtgnrtrtjrirtjgrngrogorjgorhgrhr"

REMEMBER_COOKIE_DURATION = timedelta(days=30)

SQLALCHEMY_TRACK_MODIFICATION = False
SQLALCHEMY_DATABASE_URI = "postgresql://vqklygsa:5C42T__du4u1BsNdcbgU9e5P8jNmpGyk@cornelius.db.elephantsql.com/vqklygsa"
conn = psycopg2.connect(user="vqklygsa", password='5C42T__du4u1BsNdcbgU9e5P8jNmpGyk', host='cornelius.db.elephantsql.com', port='5432')
