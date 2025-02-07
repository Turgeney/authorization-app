from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request



from app.routes import router as APIRouter
import pytz

app = FastAPI()

#Указание на обработчики HTTP запросов (views, endpoints)
app.include_router(APIRouter)

# Монтирование директории со статичными файлами
app.mount("/static", StaticFiles(directory="static"), name="static")


# Используем зависимость OAuth2, но без полной реализации OAuth2
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

