from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post("/analyze", json={
        "student_id": "123",
        "document_text": "This is a sample essay.",
        "rubric_id": "default"
    })
    assert response.status_code == 200
    assert "grade" in response.json()
    assert "feedback" in response.json()
