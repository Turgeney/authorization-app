from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.jwt_functions import *
from app.models import User
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

# Указание директории с шаблонами HTML
templates = Jinja2Templates(directory="templates")

@router.get("/test", response_class=HTMLResponse)
async def get(request: Request):
    # тест Jinja2 template engine
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/")
async def login(user: User):
    # Здесь нужно добавить проверку пользователя
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/protected")
async def secure_data(token: str = Depends(oauth2_scheme)):
     decode_access_token(token)
     return {"message": "This is secure data"}