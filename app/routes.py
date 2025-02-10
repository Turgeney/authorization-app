from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.jwt_functions import *
from app.models import User, Token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

# Указание директории с шаблонами HTML
templates = Jinja2Templates(directory="templates")

#Основная страница
@router.get("/", response_class=HTMLResponse)
async def get(request: Request):
    # тест Jinja2 template engine
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Пример проверки логина и пароля
    if form_data.username != "test" or form_data.password != "test":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    # Генерация JWT (здесь необходимо заменить secret и алгоритм на ваши собственные)
    access_token = jwt.encode({"sub": form_data.username}, "secret", algorithm="HS256")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/data")
async def secure_data(token: str = Depends(oauth2_scheme)):
     print(token)
     decode_access_token(token)
     return {"message": "Access Granted!"}  