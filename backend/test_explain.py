from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_ai_explain():
    response = client.post("/api/ai/explain", json={
        "question": "What is the powerhouse of the cell?",
        "user_answer": "Nucleus",
        "correct_answer": "Mitochondria",
        "understanding_level": "ELI5"
    })
    assert response.status_code == 200
    data = response.json()
    assert "explanation" in data
