from pydantic import BaseModel
from app.main import *
from app.database import AuthDB
from sqlalchemy import Column, Integer, String


class User(AuthDB):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    """Модель для ответа"""
    access_token: str
    token_type: str