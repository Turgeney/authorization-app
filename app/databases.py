#Работа с базами данных
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import AUTH_DATABASE_LOC

engine = create_engine(AUTH_DATABASE_LOC)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AuthDB = declarative_base()

def get_AuthDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   
