from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "SecurePass123"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_user_invalid_email():
    response = client.post("/users/", json={
        "name": "John Doe",
        "email": "invalid-email",
        "password": "SecurePass123"
    })
    assert response.status_code == 422
