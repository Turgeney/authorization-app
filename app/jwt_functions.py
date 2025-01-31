# операции с jwt
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta
from main import *

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Создание токена. Опционально указывается срок его жизни. 
    По умолчанию - 15 минут
    """                      
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.now(datetime.timezone.utc)+ timedelta(minutes=15)
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