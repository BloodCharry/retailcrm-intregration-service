import pytest
from fastapi.testclient import TestClient
from decimal import Decimal
from app.main import app

client = TestClient(app)


def test_create_payment_endpoint(monkeypatch):
    async def fake_create_payment(self, data):
        return {
            "id": 1,
            "order_id": data.order_id,
            "amount": str(data.amount),  # сериализация Decimal
            "type": data.type,
        }

    from app.services import payments
    monkeypatch.setattr(payments.PaymentService, "create_payment", fake_create_payment)

    payload = {"order_id": 1, "amount": "99.99", "type": "card"}
    response = client.post("/api/v1/payments", json=payload, headers={"X-API-KEY": "test"})
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == 1
    assert data["amount"] == "99.99"
    assert data["type"] == "card"
