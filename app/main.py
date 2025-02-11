#основной
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.databases import engine, AuthDB
from app.routes import router as APIRouter
from app.constants import STATIC_DIR

AuthDB.metadata.create_all(bind=engine)

app = FastAPI()

#Указание на обработчики HTTP запросов (views, endpoints)
app.include_router(APIRouter)

# Монтирование директории со статичными файлами
app.mount(STATIC_DIR, StaticFiles(directory="static"), name="static")

