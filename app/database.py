from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.constants import AUTH_DATABASE_STR

engine = create_engine(AUTH_DATABASE_STR)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AuthDB = declarative_base()


   
