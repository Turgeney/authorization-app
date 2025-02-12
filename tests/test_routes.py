import pytest
from fastapi.testclient import TestClient
from app.main import app 
from app.utils import create_access_token
from tests.utils_t import generate_random_string

client = TestClient(app)

def test_main_page():
    response = client.get("/")
    assert response.status_code == 200

def test_register():
    mock_data = {
        "username": generate_random_string(8),
        "password": generate_random_string(8)
    }    
    response = client.post("/login", data=mock_data)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["message"] == "Пользователь успешно зарегистрирован."

def test_login():
    mock_data = {
        "username": "test",
        "password": "test"
    }
    response = client.post("/login", data=mock_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"

def test_check_access():
    testkey = generate_random_string(8)
    testvalue = generate_random_string(10)
    mock_data = {
        testkey: testvalue,
    }
    jwt_token = create_access_token(mock_data)  
    headers = {
        "Authorization": f"Bearer {jwt_token}"
    }
    response = client.get("/check_access", headers=headers)
    payload_data = response.json()
    del payload_data['exp']
    assert response.status_code == 201
    assert payload_data == mock_data 
