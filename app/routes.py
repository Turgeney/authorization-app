#entry-points, методы rest api
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer#, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.models import RequestUser, User, ResponseToken
from app.databases import get_AuthDB
from app.settings import TEMPLATE_DIR
from app.utils import hash_create, hash_check, create_access_token, decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

# Указание директории с шаблонами HTML
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    """Основная страница"""
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/register", response_model=RequestUser)
def register_user(incoming_user: RequestUser, AuthDB: Session = Depends(get_AuthDB)):
    """Регистрация нового пользователя
    должны передаваться username и password
    """
    exist_user = AuthDB.query(User).filter(User.username == incoming_user.username).first()
    if exist_user:
        raise HTTPException(status_code=400, detail="Такой пользователь уже существует")
    hashed_password = hash_create(incoming_user.password)
    new_user = User(username=incoming_user.username, hashed_password=hashed_password)
    AuthDB.add(new_user)
    AuthDB.commit()
    AuthDB.refresh(new_user)
    return JSONResponse(content={"message": "Пользователь успешно зарегистрирован."}, status_code=201)

@router.post("/login", response_model=ResponseToken)
def login(incoming_user: RequestUser, AuthDB: Session = Depends(get_AuthDB)):
    """Вход существующео пользователя
    должны передаваться username и password
    возвращает access_token и token_type: bearer
    """
    exist_user = AuthDB.query(User).filter(User.username == incoming_user.username).first()
    if not exist_user:
        raise HTTPException(status_code=401, detail="Неверные имя пользователя или пароль")
    check_result = hash_check(subj_password = incoming_user.password, hashed_password = exist_user.hashed_password)
    if not check_result:
        raise HTTPException(status_code=401, detail="Неверные имя пользователя или пароль")
    access_token = create_access_token({"subj":exist_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
    
@router.get("/check_access")
async def check_access(token: str = Depends(oauth2_scheme)):
     """Проверка прав доступа и jwt
     должен передаваться jwt
     """
     payload = decode_access_token(token)
     return JSONResponse(content={"payload": payload}, status_code=201)