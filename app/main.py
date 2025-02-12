#основной
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.databases import engine, AuthDB
from app.routes import router as APIRouter
from app.settings import STATIC_DIR, ORIGINS

AuthDB.metadata.create_all(bind=engine)

app = FastAPI()

#Указание на обработчики HTTP запросов (views, endpoints)
app.include_router(APIRouter)

# Монтирование директории со статичными файлами
app.mount(STATIC_DIR, StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)