import pytest
from fastapi.testclient import TestClient
from decimal import Decimal
from app.main import app

client = TestClient(app)


def test_list_orders_endpoint(monkeypatch):
    async def fake_list_orders(self, filters, page, limit):
        return {"orders": [{"id": 1, "number": "ORD-001"}]}

    from app.services import orders
    monkeypatch.setattr(orders.OrderService, "list_orders", fake_list_orders)

    response = client.get("/api/v1/orders", headers={"X-API-KEY": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "orders" in data
    assert data["orders"][0]["number"] == "ORD-001"


def test_create_order_endpoint(monkeypatch):
    async def fake_create_order(self, data):
        return {
            "id": 1,
            "number": data.number,
            "customer_id": data.customer_id,
            "items": [item.model_dump() for item in data.items],
        }

    from app.services import orders
    monkeypatch.setattr(orders.OrderService, "create_order", fake_create_order)

    payload = {
        "number": "ORD-002",
        "customer_id": 42,
        "items": [{"offer_id": 1, "quantity": 2, "price": "99.99"}],
    }
    response = client.post("/api/v1/orders", json=payload, headers={"X-API-KEY": "test"})
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == "ORD-002"
    assert data["customer_id"] == 42
    assert data["items"][0]["offer_id"] == 1
