# операции с jwt
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta
from app.constants import *
from main import *
from typing import Optional

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Создание токена. Опционально указывается срок его жизни. 
    По умолчанию - 15 минут
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
    """Декодирование токена. 
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