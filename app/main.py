from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine, AuthDB
from app.models import User
from app.routes import router as APIRouter
import pytz

app = FastAPI()

#Указание на обработчики HTTP запросов (views, endpoints)
app.include_router(APIRouter)

# Монтирование директории со статичными файлами
app.mount("/static", StaticFiles(directory="static"), name="static")

AuthDB.metadata.create_all(bind=engine)