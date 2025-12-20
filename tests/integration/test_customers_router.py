import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_customers_endpoint(monkeypatch):
    async def fake_list_customers(self, filters, page, limit):
        return {"customers": [{"id": 1, "firstName": "Alice"}]}

    from app.services import customers
    monkeypatch.setattr(customers.CustomerService, "list_customers", fake_list_customers)

    response = client.get("/api/v1/customers", headers={"X-API-KEY": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "customers" in data
    assert data["customers"][0]["firstName"] == "Alice"


def test_create_customer_endpoint(monkeypatch):
    async def fake_create_customer(self, data):
        return {"id": 1, "firstName": data.firstName, "email": data.email}

    from app.services import customers
    monkeypatch.setattr(customers.CustomerService, "create_customer", fake_create_customer)

    payload = {"firstName": "Bob", "email": "bob@example.com"}
    response = client.post("/api/v1/customers", json=payload, headers={"X-API-KEY": "test"})
    assert response.status_code == 200
    data = response.json()
    assert data["firstName"] == "Bob"
    assert data["email"] == "bob@example.com"
