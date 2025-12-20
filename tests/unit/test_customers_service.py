import pytest
from app.services.customers import CustomerService
from app.schemas.customers import CustomerCreate


class DummyCRM:
    async def list_customers(self, filters, page, limit):
        return {"ok": True, "filters": filters, "page": page, "limit": limit}

    async def create_customer(self, data):
        return {"ok": True, "customer": data}


@pytest.mark.asyncio
async def test_list_customers_returns_data():
    crm = DummyCRM()
    service = CustomerService(crm)

    result = await service.list_customers({"email": "test@example.com"}, page=1, limit=20)
    assert result["ok"] is True
    assert result["filters"]["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_create_customer_returns_data():
    crm = DummyCRM()
    service = CustomerService(crm)

    customer = CustomerCreate(firstName="Alice", email="alice@example.com")
    result = await service.create_customer(customer)

    assert result["ok"] is True
    assert result["customer"]["firstName"] == "Alice"
    assert result["customer"]["email"] == "alice@example.com"
