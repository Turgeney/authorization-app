from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from pydantic import BaseModel
from typing import Optional

from app.routes import router as APIRouter


# Секретный ключ для подписи JWT
SECRET_KEY = "my test key"

app = FastAPI()

#Указание на обработчики HTTP запросов (views, endpoints)
app.include_router(APIRouter)

# Монтирование директории со статичными файлами
app.mount("/static", StaticFiles(directory="static"), name="static")


# Используем зависимость OAuth2, но без полной реализации OAuth2
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

