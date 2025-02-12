#Операции с хэшем и jwt
from fastapi import HTTPException

from datetime import datetime, timedelta
from typing import Optional
import jwt
from passlib.context import CryptContext
import bcrypt

from app.settings import LOCAL_TIMEZONE, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_create(password:str):
    """Возвращает хэш пароля для сохранения в БД
    password - пароль
    """
    # Генерация соли
    salt = bcrypt.gensalt()
    # Хэширование пароля с использованием соли, и кодирование в utf-8
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    return hashed_password

def hash_check(subj_password:str, hashed_password:str):
    """проверка хэша пароля
    Возвращает True, если пароль соответствует хэшу
    subj_password - проверяемый пароль
    hashed_password - хэш, с которым сверяемся
    """
    result = bcrypt.checkpw(subj_password.encode('utf-8'), hashed_password.encode('utf-8'))
    return result


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Возвращает кодированный access JWT
    data - словарь, из которого будет построен token 
    expires_delta - Опционально указывается срок его жизни (тег exp). По умолчанию - 15 минут
    """
    current_time = datetime.now(LOCAL_TIMEZONE)                      
    to_encode = data.copy()
    if expires_delta:
        expire = current_time + expires_delta
    else:
        expire = current_time + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

# Проверка JWT-токена
def decode_access_token(token: str):
    """Вовращает payload полезную нагрузку access JWT
    При успешном декодировании возвращает payload.
    Иначе - ошибка 401
    """          
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")