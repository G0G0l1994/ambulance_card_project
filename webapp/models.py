from sqlalchemy import Column, Integer, String, Date, Text
from webapp.db import Base, engine 

#-------------------Основные сущности-------------------
class DiagnosisCode(Base):
    __tablename__ = "МКБ-10"
    
    id = Column(Integer, primary_key = True)
    code = Column(Text)

    def __repr__(self):
        return f'{self.code}'
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

#-------------------Раздел составных частей карт-------------------


