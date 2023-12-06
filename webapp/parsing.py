from webapp import db_session
from webapp.models import DiagnosisCode

query_code = DiagnosisCode.query.all()

if __name__ == "__main__":
    for item in query_code:
        print(item.code)
    
    
        
    
    
        