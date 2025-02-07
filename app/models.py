from pydantic import BaseModel
from main import *



class User(BaseModel):
    """Модель данных пользователя
"""
    username: str
    password: str
