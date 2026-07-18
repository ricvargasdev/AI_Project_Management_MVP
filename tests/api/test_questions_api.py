from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_question_endpoint_returns_answer():

    response = client.post(
        "/questions",
        json={
            "customer": "MHP",
            "question": "When did they request Apple Pay?"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body