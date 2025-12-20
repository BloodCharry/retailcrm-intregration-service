import pytest
from decimal import Decimal
from app.services.payments import PaymentService
from app.schemas.payments import PaymentCreate


class DummyCRM:
    async def create_payment(self, data):
        return {"ok": True, "payment": data}


@pytest.mark.asyncio
async def test_create_payment_returns_data():
    crm = DummyCRM()
    service = PaymentService(crm)

    payment = PaymentCreate(order_id=1, amount=Decimal("99.99"), type="card")
    result = await service.create_payment(payment)

    assert result["ok"] is True
    assert result["payment"]["order_id"] == 1
    assert result["payment"]["amount"] == Decimal("99.99")
    assert result["payment"]["type"] == "card"
