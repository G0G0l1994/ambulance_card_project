from webapp.db import db_session

def save_card():
    
    db_session.bulk_insert_mapping(return_defaults=True)
    db_session.commit()
    pass