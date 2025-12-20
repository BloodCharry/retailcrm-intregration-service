import pytest
from decimal import Decimal
from app.services.payments import PaymentService
from app.schemas.payments import PaymentCreate
from tests.dummies import DummyCRM


@pytest.mark.asyncio
async def test_create_payment_returns_data():
    crm = DummyCRM()
    service = PaymentService(crm)

    payment = PaymentCreate(order_id=1, amount=Decimal("99.99"), type="card")
    result = await service.create_payment(payment)

    assert result["ok"] is True
    assert result["payment"]["order"]["id"] == 1
    assert result["payment"]["amount"] == "99.99"
    assert result["payment"]["type"] == "card"
