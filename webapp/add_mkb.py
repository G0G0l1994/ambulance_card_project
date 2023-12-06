from webapp.db import db_session
from webapp.models import DiagnosisCode

    

def read_file(filename):
    data = []
    with open(filename,'r',encoding='utf-8') as f:
        for line in f.readlines():
            data.append(line.rstrip())
    for item in data:
        save_mkb(item)
    print("done")
    

def save_mkb(item):
    code = DiagnosisCode(code = item)
    db_session.add(code)
    print(f"Код {item} обновлен")
    db_session.commit()
    db_session.close()

if __name__ == "__main__":
    read_file("mkb_10.txt")