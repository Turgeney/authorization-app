#модели, классы
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from app.main import *
from app.databases import AuthDB

# region модели бд

class User(AuthDB):
    """Модель пользователя в бд
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# endregion

# region модели вне бд

class RequestUser(BaseModel):
    """класс пользователя для входящих данных"""
    username: str
    password: str

class ResponseToken(BaseModel):
    """класс jwt токена для исходящих данных"""
    access_token: str
    token_type: str

# endregion