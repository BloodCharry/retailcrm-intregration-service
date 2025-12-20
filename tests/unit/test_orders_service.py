import pytest
from decimal import Decimal
from app.services.orders import OrderService
from app.schemas.orders import OrderCreate, OrderItem


class DummyCRM:
    async def list_orders(self, filters, page, limit):
        return {"ok": True, "filters": filters, "page": page, "limit": limit}

    async def create_order(self, data):
        return {"ok": True, "order": data}


@pytest.mark.asyncio
async def test_list_orders_returns_data():
    crm = DummyCRM()
    service = OrderService(crm)

    result = await service.list_orders({"number": "123"}, page=1, limit=10)
    assert result["ok"] is True
    assert result["filters"]["number"] == "123"


@pytest.mark.asyncio
async def test_create_order_returns_data():
    crm = DummyCRM()
    service = OrderService(crm)

    order = OrderCreate(
        number="ORD-001",
        customer_id=42,
        items=[OrderItem(offer_id=1, quantity=2, price=Decimal("99.99"))],
    )
    result = await service.create_order(order)

    assert result["ok"] is True
    assert result["order"]["number"] == "ORD-001"
    assert result["order"]["customer_id"] == 42
    assert result["order"]["items"][0]["offer_id"] == 1