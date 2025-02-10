import pytest
from fastapi.testclient import TestClient
from app.main import app  # импортируем ваше приложение FastAPI
from app.models import Token
from app.jwt_functions import create_access_token

client = TestClient(app)

def test_read_test_page():
    response = client.get("/test")
    assert response.status_code == 200

def test_secure_data():
    mock_data = {
        "username": "test",
        "password": "test"
    }
    jwt_token = create_access_token(mock_data)  
    headers = {
        "Authorization": f"Bearer {jwt_token}"
    }
    response = client.get("/protected", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Access Granted!"}

def test_login():
    # Создаем данные формы для отправки
    mock_data = {
        "username": "test",
        "password": "test"
    }

    # Посылаем POST-запрос на маршрут /login, передавая данные формы
    response = client.post("/login", data=mock_data)

    # Проверяем, что статус ответа 200 OK
    assert response.status_code == 200

    # Преобразуем ответ в JSON и проверяем поля
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"