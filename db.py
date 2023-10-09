from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.dialects import postgresql
import psycopg2

engine = create_engine("postgresql://vqklygsa:5C42T__du4u1BsNdcbgU9e5P8jNmpGyk@cornelius.db.elephantsql.com/vqklygsa")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

