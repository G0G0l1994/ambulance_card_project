from datetime import timedelta
import psycopg2
SECRET_KEY = "ewfrejugjrtgbjrtbtrhnbnrtbnttbtjgijitgejv nrjergegtgnrtrtjrirtjgrngrogorjgorhgrhr"

REMEMBER_COOKIE_DURATION = timedelta(days=30)
SQLALCHEMY_TRACK_MODIFICATION = False
SQLALCHEMY_DATABASE_URI = "postgresql://vqklygsa:5C42T__du4u1BsNdcbgU9e5P8jNmpGyk@cornelius.db.elephantsql.com/vqklygsa"
conn = psycopg2.connect(user="vqklygsa", password='5C42T__du4u1BsNdcbgU9e5P8jNmpGyk', host='cornelius.db.elephantsql.com', port='5432')
